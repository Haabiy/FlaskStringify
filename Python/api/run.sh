#!/bin/bash

# Build the Docker image
docker build -t flask-web-service .

# Run the Docker container
docker run -d -p 12345:12345 --name flask-app flask-web-service