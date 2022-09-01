#!/bin/bash

sudo yum check-update -y
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd.service