#!/bin/bash

fs = "$(blkid | awk ' { print $4 } '"

blkid | awk -F"=" '/UUID=/ { print $3 }' | grep -o '\w*-\w*-\w*-\w*-\w*'

if []

sudo mkfs -t xfs /dev/xvdf
sudo mkdir /data
sudo mount /dev/xvdf /data

sudo cp /etc/fstab /etc/fstab.orig
blkid | egrep "/dev/xvdf: UUID="
echo "UUID=xxx"

# https://stackoverflow.com/questions/43889158/shell-script-to-list-unformatted-disks-partitions