#!/bin/bash
set -e

APP_DIR="/home/ubuntu/mlops-71052402033"
cd "$APP_DIR"

docker build -t student-result-predictor .

# Remove the old container if it exists
docker rm -f student-result-predictor 2>/dev/null || true

# Stop Nginx if it occupies port 80
systemctl stop nginx 2>/dev/null || true

# Run the application container
docker run -d --name student-result-predictor --restart unless-stopped -p 80:5000 student-result-predictor
