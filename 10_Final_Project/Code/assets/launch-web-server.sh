#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd.service
echo '<html><h1>Hello From The Web Server!</h1></html>' > /var/www/html/index.html
