#!/bin/bash
export TARGET_URL="THISISTHETARGETURL"
apt-get update
apt-get install -y python3
apt-get install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get update -y
apt-get install -y python-dev build-essential python-pip
apt install -y awscli
pip install --upgrade pip
mkdir ~/.aws
printf "[default]\naws_access_key_id = REPLACEHERE\naws_secret_access_key = REPLACEHERE" >> ~/.aws/credentials
aws s3 cp s3://scrape-fall2018/scraper.py ~/
aws s3 cp s3://scrape-fall2018/requirements.txt ~/
pip install -r requirements.txt
apt-get install -y libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome*.deb
pip install -U pychrome --upgrade --user
google-chrome --headless --disable-gpu --remote-debugging-port=9222 &
python scraper.py
