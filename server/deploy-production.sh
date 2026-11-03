#!/usr/bin/env bash
# Deploy the v2 site to PRODUCTION (zwicoat.com). Same upload as staging:
# both vhosts serve /home/ubuntu/zwicoat-v2/dist, so one upload updates both.
#   bash server/deploy-production.sh            # build locally, upload, swap dist
#   bash server/deploy-production.sh --no-build
# The Apache vhosts were pointed at zwicoat-v2/dist by remote-production-swap.sh
# (2026-11-02). Rollback of the vhosts: see the comments in that script.
set -euo pipefail
exec bash "$(dirname "$0")/deploy-staging.sh" "$@"
