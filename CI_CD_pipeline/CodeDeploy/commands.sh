#!/bin/bash

# Installing CodeDeploy Agent
sudo yum update
sudo yum install ruby

# Download the agent (replace the region)
wget https://aws-codedeploy-eu-west-3.s3.eu-west-3.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status



# uninstalling apache
# Stop Apache
sudo systemctl stop httpd

# Disable Apache from starting at boot
sudo systemctl disable httpd

# Remove Apache (httpd)
sudo yum remove -y httpd

# Delete any leftover files in the web root
sudo rm -rf /var/www/html/*

# (Optional) Delete your install script logs or temp files if needed
