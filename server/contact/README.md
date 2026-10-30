# zwicoat.com contact endpoint

A small Flask app that receives the contact form and emails it to info@zwicoat.com. No third-party form service. It runs on the same EC2 box as the site, behind Apache.

- `POST /api/contact` takes JSON or form fields: `name`, `organization`, `email`, `device`, `material`, `message`, and a honeypot `website` that must be empty.
- `GET /api/contact/health` returns `{"ok": true}`.
- JSON requests get JSON back. Plain form posts get a 303 redirect to `/contact?sent=1#form-sent` or `/contact?error=1#form-error`. The fragment lets the static page show the message without JavaScript.
- Rules: name and a valid email are required, the message is 10 to 4000 characters, the honeypot must be empty, and each IP gets 5 messages per hour. Line breaks and control characters are stripped from every header field.
- No CORS headers, so only the same origin can call it. `DEV_CORS=1` is for local development only.

## Deploy steps

Run these on the EC2 box (the same one that serves zwicoat.com). Python 3.10 or newer is needed. Ubuntu already has it for the Django site.

1. Copy the files.

   ```bash
   mkdir -p /home/ubuntu/zwicoat-contact
   # from your machine, in the project root:
   scp -r server/contact/* ubuntu@<ec2-host>:/home/ubuntu/zwicoat-contact/
   ```

2. Create the virtual environment.

   ```bash
   cd /home/ubuntu/zwicoat-contact
   python3 -m venv venv
   ```

3. Install the requirements.

   ```bash
   ./venv/bin/pip install -r requirements.txt
   ```

4. Write the env file. Pick the SMTP values from "Which SMTP to use" below.

   ```bash
   sudo cp zwicoat-contact.env.example /etc/zwicoat-contact.env
   sudo nano /etc/zwicoat-contact.env      # fill SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, MAIL_FROM
   sudo chown root:root /etc/zwicoat-contact.env
   sudo chmod 600 /etc/zwicoat-contact.env
   ```

5. Enable and start the service.

   ```bash
   sudo cp zwicoat-contact.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now zwicoat-contact
   sudo systemctl status zwicoat-contact
   curl http://127.0.0.1:5057/api/contact/health
   ```

6. Add the Apache snippet. Enable the proxy modules once, then paste the two lines from `apache-snippet.conf` inside the VirtualHost in `/etc/apache2/sites-available/zwicoat.conf`. If certbot created a separate `zwicoat-le-ssl.conf`, add them inside its VirtualHost too. The box also serves Dumbo Press, so edit only the zwicoat file, not `apache2.conf`.

   ```bash
   sudo a2enmod proxy proxy_http
   sudo nano /etc/apache2/sites-available/zwicoat.conf
   ```

   ```apache
   ProxyPass /api/contact http://127.0.0.1:5057/api/contact
   ProxyPassReverse /api/contact http://127.0.0.1:5057/api/contact
   ```

7. Check the config and reload Apache.

   ```bash
   sudo apache2ctl configtest
   sudo systemctl reload apache2
   ```

8. Test with curl. The first command checks the proxy. The second sends a real message to MAIL_TO.

   ```bash
   curl https://zwicoat.com/api/contact/health

   curl -i -X POST https://zwicoat.com/api/contact \
     -H 'Content-Type: application/json' \
     -d '{"name":"Test","email":"you@example.com","device":"Sensors","message":"Test message from curl, please ignore.","website":""}'
   ```

   Expect `{"ok":true}` and an email in the info@zwicoat.com inbox with Reply-To set to the test address. If the send fails, read the log:

   ```bash
   sudo journalctl -u zwicoat-contact -n 50 --no-pager
   ```

To update later, copy the new `app.py` over and run `sudo systemctl restart zwicoat-contact`.

The service runs one gunicorn worker on purpose. The rate limiter keeps its counts in memory, so more workers would each keep their own count. A restart clears the counts.

## Which SMTP to use

Not chosen here. The three options:

**Google Workspace SMTP with an app password.** Use this if info@zwicoat.com is a Google Workspace mailbox. Host `smtp.gmail.com`, port 587 (STARTTLS) or 465 (SSL). The user is the full mailbox address. The password is a Google app password, which needs 2-Step Verification on that account. The account must be allowed to make app passwords in the Workspace admin settings. Google sends as that account, so `MAIL_FROM` should be the same address. The limit is about 2,000 messages a day, far above what this form needs.

**Amazon SES SMTP credentials.** The company already uses AWS. Create SMTP credentials in the SES console (they are separate from the IAM keys). The SMTP host is regional, for example `email-smtp.us-east-2.amazonaws.com`, port 587 or 465. Verify the sending domain zwicoat.com (or the single address used as `MAIL_FROM`) in SES, and add the DKIM records in Route53. New SES accounts start in the sandbox, which only delivers to verified addresses, so request production access or verify info@zwicoat.com as a recipient. Check that the SES region matches the host you use.

**Plain SMTP from the mail host.** Use the SMTP server of whoever hosts the zwicoat.com mailboxes. Get the host, port, username and password from them. Port 587 with STARTTLS or 465 with SSL both work. `MAIL_FROM` has to be an address that server allows you to send as. Check that SPF for zwicoat.com covers the server so messages are not marked as spam.

In all three cases, set `MAIL_TO=info@zwicoat.com` and keep the visitor's address in Reply-To, which the app does by itself.

## Testing locally

Python 3.10 or newer.

```bash
cd server/contact
python -m venv .venv
.venv/bin/pip install -r requirements.txt        # Windows: .venv\Scripts\pip
DRY_RUN=1 DEV_CORS=1 .venv/bin/python app.py     # listens on 127.0.0.1:5057
```

On PowerShell:

```powershell
$env:DRY_RUN = "1"; $env:DEV_CORS = "1"; .venv\Scripts\python app.py
```

`DRY_RUN=1` prints each message to the terminal and sends nothing.

To try the form on the Astro dev server, create `site/.env` with:

```
PUBLIC_FORM_ENDPOINT=http://127.0.0.1:5057/api/contact
```

then run `npm run dev` in `site/` and open `http://localhost:4321/contact`. In dev, the page (port 4321) and the endpoint (port 5057) are different origins, so the browser makes a cross-origin request. `DEV_CORS=1` makes the Flask app allow `http://localhost:4321` and `http://127.0.0.1:4321`. Never set `DEV_CORS` in production, where the form and the endpoint share an origin. Restart `npm run dev` after changing `site/.env`.

Without JavaScript in the dev setup, the plain form post redirects to `/contact` on port 5057, which does not exist. That redirect only works in production, where both are on zwicoat.com.

Quick curl test against the local app:

```bash
curl -i -X POST http://127.0.0.1:5057/api/contact \
  -H 'Content-Type: application/json' \
  -d '{"name":"Test","email":"you@example.com","device":"Sensors","message":"Test message, please ignore.","website":""}'
```
