#!/bin/bash

# Update package index
apt-get update -y

# Install nginx
apt-get install nginx -y

# Check if nginx installation was successful
if [ $? -ne 0 ]; then
    echo "Error: Nginx installation failed."
    exit 1
fi

# Create a simple HTML file
echo "Hello World!" > /var/www/html/index.html

# Start nginx service
service nginx start

# Check if nginx service started successfully
if [ $? -ne 0 ]; then
    echo "Error: Failed to start nginx service."
    exit 1
else
    echo "Nginx installation and configuration completed successfully."
fi
