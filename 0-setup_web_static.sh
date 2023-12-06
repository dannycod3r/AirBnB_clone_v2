#!/usr/bin/env bash
# bash script that setup web servers for web_static deployment

# install nginx if not installed
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# create data folder and sub folders
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir /data/web_static/releases/test

# create file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# sybolic link to point to /data/web_static/releases/test/
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# ownership to
sudo chown -R ubuntu:ubuntu /data/

# configure nginx to server /data/web_static/current/ to hbnb_static
# eg https://mydomainname.tech/hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
