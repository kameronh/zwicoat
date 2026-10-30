#!/usr/bin/env bash
# Deploy the v2 site to the EC2 box as a STAGING vhost (staging.zwicoat.com).
# Run from the project root on the dev machine (Git Bash). Does NOT touch the
# live zwicoat.com vhost. Production swap is a separate, explicit step.
#
#   bash server/deploy-staging.sh            # build, upload, configure staging
#   bash server/deploy-staging.sh --no-build # upload the existing site/dist
#
# Requirements: ~/.ssh/zcmi-ec2.pem, the box reachable as $HOST, node locally.
set -euo pipefail
HOST="ubuntu@ec2-3-131-73-139.us-east-2.compute.amazonaws.com"
KEY="$HOME/.ssh/zcmi-ec2.pem"
REMOTE_DIR="/home/ubuntu/zwicoat-v2"
SSH="ssh -i $KEY -o ConnectTimeout=20 $HOST"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ "${1:-}" != "--no-build" ]]; then
  echo "== building site"
  (cd "$ROOT/site" && npm run build >/dev/null)
fi
test -f "$ROOT/site/dist/index.html" || { echo "no dist/index.html"; exit 1; }

echo "== uploading dist and server files"
$SSH "mkdir -p $REMOTE_DIR/dist.new $REMOTE_DIR/server"
tar -C "$ROOT/site/dist" -czf - . | $SSH "tar -C $REMOTE_DIR/dist.new -xzf -"
tar -C "$ROOT/server" -czf - contact | $SSH "tar -C $REMOTE_DIR/server -xzf -"
scp -q -i "$KEY" "$ROOT/server/remote-staging-setup.sh" "$HOST:$REMOTE_DIR/remote-staging-setup.sh"

echo "== switching dist atomically and running remote setup"
$SSH "cd $REMOTE_DIR && rm -rf dist.old && { [ -d dist ] && mv dist dist.old || true; } && mv dist.new dist && bash remote-staging-setup.sh"
echo "== done. Staging vhost serves $REMOTE_DIR/dist for staging.zwicoat.com"
