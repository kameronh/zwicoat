#!/usr/bin/env bash
# Runs ON the EC2 box. Points the live zwicoat.com vhosts at the v2 build
# (/home/ubuntu/zwicoat-v2/dist), keeps the old site on disk for rollback,
# adds the contact-endpoint proxy, drops the old SPA FallbackResource.
# Rollback: sudo cp /etc/apache2/sites-available/zwicoat.conf.bak-v1 /etc/apache2/sites-available/zwicoat.conf
#           sudo cp /etc/apache2/sites-available/zwicoat-le-ssl.conf.bak-v1 /etc/apache2/sites-available/zwicoat-le-ssl.conf
#           sudo systemctl reload apache2
set -euo pipefail
NEWROOT=/home/ubuntu/zwicoat-v2/dist
for f in zwicoat.conf zwicoat-le-ssl.conf; do
  P=/etc/apache2/sites-available/$f
  [ -f "$P.bak-v1" ] || sudo cp "$P" "$P.bak-v1"
  sudo sed -i "s#DocumentRoot /home/ubuntu/zwicoat/dist#DocumentRoot $NEWROOT#; s#<Directory /home/ubuntu/zwicoat/dist>#<Directory $NEWROOT>#" "$P"
  sudo sed -i 's#^\(\s*\)FallbackResource /index.html#\1ErrorDocument 404 /404.html#' "$P"
  if ! grep -q "ProxyPass /api/contact" "$P"; then
    sudo sed -i "s#^\(\s*\)ErrorDocument 404 /404.html#\1ErrorDocument 404 /404.html\n\1ProxyPass /api/contact http://127.0.0.1:5057/api/contact\n\1ProxyPassReverse /api/contact http://127.0.0.1:5057/api/contact#" "$P"
  fi
done
sudo a2enmod -q proxy proxy_http headers >/dev/null 2>&1 || true
sudo apache2ctl configtest
sudo systemctl reload apache2
echo "production now serves $NEWROOT"
grep -n "DocumentRoot\|ProxyPass \|ErrorDocument" /etc/apache2/sites-available/zwicoat-le-ssl.conf
