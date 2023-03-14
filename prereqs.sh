#!/bin/bash

sudo apt update
sudo apt upgrade
sudo apt install -y python3-picamera2 ffmpeg lighttpd
echo "####"
echo "Rebooting automatically in 60 seconds. Ctrl+C to cancel"
echo "####"
read -t 60
sudo init 6