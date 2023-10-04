#!/usr/bin/env bash
# Bash script that sets up a web servers for the deployment of web_static

# Prepare my web server
if [ "$(dpkg -l | grep -c 'ii  nginx  ')" -eq 0 ]; then
        sudo apt-get update
        sudo apt-get install nginx -y
fi

# Create folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/


# Create a simple HTML file
sudo echo 'Hellooooooooo World!' | sudo tee /data/web_static/releases/test/index.html

# Create the symbolic link
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_conf="/etc/nginx/sites-available/default"
nginx_alias="\n\tlocation /hbnb_static/ { \n\t\talias /data/web_static/current/;\n\t }"
sudo sed -i "/^\tserver_name _;/i\\$nginx_alias" $nginx_conf

# Restart Nginx
sudo service nginx restart
