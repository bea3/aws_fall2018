#!/bin/bash
usermod -a -G apache ubuntu
export TARGET_URL="THISISTHETARGETURL"
apt-get update
apt-get install -y python3
apt-get install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get update -y
apt-get install -y python-dev build-essential python-pip
apt install -y awscli
echo "**** Retrieving scraping script and requirements.txt"
export AWS_ACCESS_KEY_ID=THISISTHEAWSKEY
export AWS_SECRET_ACCESS_KEY=THISISTHESECRETKEY
mkdir /tmp/scraper
aws s3 cp s3://scrape-fall2018/scraper.py /tmp/scraper
aws s3 cp s3://scrape-fall2018/requirements.txt /tmp/scraper
echo "**** Installing requirements"
pip install -r /tmp/scraper/requirements.txt
echo "**** Installing Google Chrome dependencies"
apt-get install -y libxss1 libappindicator1 libindicator7
echo "**** Installing Google Chrome"
cd /tmp/scraper
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y /tmp/scraper/google-chrome-stable_current_amd64.deb
echo "**** Starting Google Chrome"
google-chrome --headless --no-sandbox --disable-gpu --remote-debugging-port=9222 &
echo "**** Running scraper"
sleep 5
touch /tmp/scraper/website.json
chmod 777 /tmp/scraper/website.json
python /tmp/scraper/scraper.py
echo "**** Sending scraped elements in the bucket"
DATE=`date '+%Y-%m-%d-%H:%M:%S'`
FILENAME="$DATE.json"
aws s3 cp /tmp/scraper/website.json s3://website-elements/"$FILENAME"

