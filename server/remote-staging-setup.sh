#!/usr/bin/env bash
# Runs ON the EC2 box (uploaded by deploy-staging.sh). Idempotent.
# 1. Apache vhost for staging.zwicoat.com -> /home/ubuntu/zwicoat-v2/dist (HTTP;
#    HTTPS via certbot once the DNS record exists).
# 2. Contact endpoint service (gunicorn on 127.0.0.1:5057), DRY_RUN until an
#    SMTP env file is written by Kam.
set -euo pipefail
DIR=/home/ubuntu/zwicoat-v2
VHOST=/etc/apache2/sites-available/zwicoat-staging.conf

if [ ! -f "$VHOST" ]; then
sudo tee "$VHOST" >/dev/null <<'EOF'
<VirtualHost *:80>
    ServerName staging.zwicoat.com
    DocumentRoot /home/ubuntu/zwicoat-v2/dist
    <Directory /home/ubuntu/zwicoat-v2/dist>
        Options -Indexes +FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
    # Astro writes /route/index.html, so no FallbackResource is needed.
    ErrorDocument 404 /404.html
    ProxyPass /api/contact http://127.0.0.1:5057/api/contact
    ProxyPassReverse /api/contact http://127.0.0.1:5057/api/contact
    <IfModule mod_headers.c>
        Header set X-Robots-Tag "noindex, nofollow"
    </IfModule>
</VirtualHost>
EOF
  echo "wrote $VHOST"
fi
sudo a2enmod -q proxy proxy_http headers >/dev/null 2>&1 || true
sudo a2ensite -q zwicoat-staging >/dev/null 2>&1 || true
sudo apache2ctl configtest
sudo systemctl reload apache2

# --- contact endpoint service
APP=$DIR/server/contact
if [ ! -d "$APP/.venv" ]; then
  python3 -m venv "$APP/.venv"
fi
"$APP/.venv/bin/pip" install -q -r "$APP/requirements.txt"
if [ ! -f /etc/zwicoat-contact.env ]; then
  # DRY_RUN until Kam adds SMTP credentials (see server/contact/README.md)
  printf 'DRY_RUN=1\nMAIL_TO=info@zwicoat.com\nTRUST_PROXY=1\n' | sudo tee /etc/zwicoat-contact.env >/dev/null
  sudo chmod 600 /etc/zwicoat-contact.env
  echo "wrote /etc/zwicoat-contact.env (DRY_RUN=1)"
fi
sudo tee /etc/systemd/system/zwicoat-contact.service >/dev/null <<EOF
[Unit]
Description=zwicoat.com contact form endpoint
After=network.target

[Service]
User=ubuntu
WorkingDirectory=$APP
EnvironmentFile=/etc/zwicoat-contact.env
ExecStart=$APP/.venv/bin/gunicorn --workers 1 --bind 127.0.0.1:5057 app:app
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable -q zwicoat-contact
sudo systemctl restart zwicoat-contact
sleep 1
curl -s http://127.0.0.1:5057/api/contact/health || true
echo
systemctl is-active zwicoat-contact
