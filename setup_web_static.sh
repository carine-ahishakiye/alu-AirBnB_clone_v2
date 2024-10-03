#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! command -v nginx > /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
<head></head>
<body>Holberton School</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i '/^server {/a \\
        \n    location /hbnb_static {\n        alias /data/web_static/current/;\n        index index.html;\n    }\n' /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo systemctl restart nginx

# Exit successfully
exit 0

