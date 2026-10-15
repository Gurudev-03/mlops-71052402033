#!/bin/bash
set -euo pipefail
cd /opt/student-app
docker build --pull -t student-app:latest .
docker rm -f student-app 2>/dev/null || true
docker run -d \
  --name student-app \
  --restart unless-stopped \
  -p 80:5000 \
  -e MODEL_VERSION=1.0 \
  student-app:latest
sleep 3
docker ps --filter name=student-app
curl --fail --silent http://127.0.0.1/ >/dev/null
echo "Student app deployed successfully."
