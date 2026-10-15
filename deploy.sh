#!/bin/bash
set -e

APP_DIR="/home/ubuntu/mlops-71052402033"
cd "$APP_DIR"

# Build the application image
docker build -t student-result-predictor .

# Remove the previous application container, if present
docker rm -f student-result-predictor 2>/dev/null || true

# Stop Nginx if it is occupying port 80
systemctl stop nginx 2>/dev/null || true

# Start the Flask application on port 80
docker run -d 
  --name student-result-predictor 
  --restart unless-stopped 
  -p 80:5000 
  student-result-predictor
