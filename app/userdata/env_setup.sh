# download Python and dependencies
apt-get update
apt-get install python3.6
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.6

# download Google Chrome
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >>> /etc/apt/sources.list
wget https://dl.google.com/linux/linux_signing_key.pub
sudo apt-key add linux_signing_key.pub
sudo apt-get update
sudo apt-get install google-chrome-stable

# download Scraper script from S3 bucket
