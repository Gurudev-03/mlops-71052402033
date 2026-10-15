#!/bin/bash
set -e

APP_DIR="/home/ubuntu/mlops-71052402033"
cd "$APP_DIR"

docker build -t student-result-predictor .
docker rm -f student-result-predictor 2>/dev/null || true
docker run -d --name student-result-predictor --restart unless-stopped -p 80:5000 student-result-predictor
