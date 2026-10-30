"""ZwiCoat contact form endpoint.

One route, POST /api/contact, sends the message to MAIL_TO over SMTP.
Run behind Apache (ProxyPass) with gunicorn. See README.md.
"""
import logging
import os
import re
import smtplib
import threading
import time
from email.message import EmailMessage

from flask import Flask, jsonify, redirect, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024  # far more than a contact message needs

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("zwicoat-contact")

EMAIL_RE = re.compile(r"^[^\s@<>,;:\"'()\[\]\\]+@[^\s@<>,;:\"'()\[\]\\]+\.[A-Za-z]{2,}$")
# Control characters, including the ones that can break out of a mail header.
CTRL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f  ]")
HEADER_BREAK_RE = re.compile(r"[\r\n\x00]+")

RATE_LIMIT = 5
RATE_WINDOW = 3600  # seconds
_hits = {}
_hits_lock = threading.Lock()

LINE_FIELDS = {"name": 200, "organization": 200, "email": 254, "material": 200}
DEVICE_MAX = 200
DEV_ORIGINS = {"http://localhost:4321", "http://127.0.0.1:4321"}


def env(name, default=""):
    return os.environ.get(name, default)


def clean_line(value, limit):
    """Single-line field: replace line breaks, drop control characters."""
    value = "" if value is None else str(value)
    value = HEADER_BREAK_RE.sub(" ", value)
    value = CTRL_RE.sub("", value)
    return value.strip()[:limit]


def clean_body(value):
    """Message body: keep newlines, drop other control characters."""
    value = "" if value is None else str(value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = "\n".join(CTRL_RE.sub("", line) for line in value.split("\n"))
    return value.strip()


def client_ip():
    # gunicorn listens on 127.0.0.1 only, so the last X-Forwarded-For value is the
    # one Apache appended. Set TRUST_PROXY=0 to use the socket address instead.
    if env("TRUST_PROXY", "1") == "1":
        xff = request.headers.get("X-Forwarded-For", "")
        if xff:
            return xff.split(",")[-1].strip()
    return request.remote_addr or "unknown"


def rate_limited(ip):
    """Return True if this IP has used its quota; otherwise record a hit."""
    now = time.time()
    with _hits_lock:
        recent = [t for t in _hits.get(ip, []) if now - t < RATE_WINDOW]
        if len(recent) >= RATE_LIMIT:
            _hits[ip] = recent
            return True
        recent.append(now)
        _hits[ip] = recent
        if len(_hits) > 5000:  # keep the dict from growing without bound
            for key in [k for k, v in _hits.items() if not v or now - v[-1] >= RATE_WINDOW]:
                _hits.pop(key, None)
    return False


def build_message(f):
    mail_from = env("MAIL_FROM") or env("SMTP_USER") or "info@zwicoat.com"
    subject = "zwicoat.com contact: " + f["name"]
    if f["device"]:
        subject += ", " + f["device"]
    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = env("MAIL_TO", "info@zwicoat.com")
    msg["Reply-To"] = f["email"]
    msg["Subject"] = subject
    msg.set_content(
        "\n".join(
            [
                "Name: " + f["name"],
                "Organization: " + f["organization"],
                "Email: " + f["email"],
                "Device type: " + f["device"],
                "Material: " + f["material"],
                "",
                "Message:",
                f["message"],
                "",
                "Sent from the zwicoat.com contact form. Reply to this email to answer the visitor.",
            ]
        )
    )
    return msg


def send_mail(msg):
    if env("DRY_RUN") == "1":
        log.info("DRY_RUN message not sent:\n%s", msg.as_string())
        return
    host = env("SMTP_HOST")
    port = int(env("SMTP_PORT", "587"))
    user = env("SMTP_USER")
    password = env("SMTP_PASS")
    if not host:
        raise RuntimeError("SMTP_HOST is not set")
    if port == 465:
        smtp = smtplib.SMTP_SSL(host, port, timeout=20)
    else:
        smtp = smtplib.SMTP(host, port, timeout=20)
    with smtp:
        smtp.ehlo()
        if port != 465:
            smtp.starttls()
            smtp.ehlo()
        if user:
            smtp.login(user, password)
        smtp.send_message(msg)


def respond(is_json, ok, status=200, error=None):
    if is_json:
        body = {"ok": ok}
        if error:
            body["error"] = error
        return jsonify(body), status
    # The fragment lets the static page show the message with CSS :target when JavaScript is off.
    return redirect("/contact?sent=1#form-sent" if ok else "/contact?error=1#form-error", code=303)


@app.after_request
def dev_cors(resp):
    # Same origin only in production (no CORS headers). DEV_CORS=1 allows the Astro dev server.
    if env("DEV_CORS") == "1":
        origin = request.headers.get("Origin", "")
        if origin in DEV_ORIGINS:
            resp.headers["Access-Control-Allow-Origin"] = origin
            resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
            resp.headers["Vary"] = "Origin"
    return resp


@app.route("/api/contact/health", methods=["GET"])
def health():
    return jsonify({"ok": True})


@app.route("/api/contact", methods=["POST", "OPTIONS"])
def contact():
    if request.method == "OPTIONS":
        # Preflight. Gets CORS headers only when DEV_CORS=1 (see dev_cors).
        return ("", 204)

    is_json = request.is_json
    data = request.get_json(silent=True) if is_json else request.form
    if not isinstance(data, dict) and not hasattr(data, "getlist"):
        return respond(is_json, False, 400, "bad request")

    def get(*names):
        for n in names:
            if data.get(n) is not None:
                return data.get(n)
        return ""

    # Honeypot: real visitors never see or fill this field.
    if str(get("website", "_gotcha")).strip():
        log.info("honeypot hit from %s", client_ip())
        return respond(is_json, False, 400, "rejected")

    f = {k: clean_line(get(k), lim) for k, lim in LINE_FIELDS.items()}
    f["device"] = clean_line(get("device", "device_type"), DEVICE_MAX)
    f["message"] = clean_body(get("message"))

    if not f["name"]:
        return respond(is_json, False, 400, "name is required")
    if not f["email"] or not EMAIL_RE.match(f["email"]):
        return respond(is_json, False, 400, "a valid email is required")
    if not 10 <= len(f["message"]) <= 4000:
        return respond(is_json, False, 400, "message must be 10 to 4000 characters")

    ip = client_ip()
    if rate_limited(ip):
        log.warning("rate limit hit from %s", ip)
        return respond(is_json, False, 429, "too many messages, try again later")

    try:
        send_mail(build_message(f))
    except Exception:
        log.exception("mail send failed")
        return respond(is_json, False, 502, "could not send")
    log.info("contact message accepted from %s", ip)
    return respond(is_json, True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(env("PORT", "5057")))
