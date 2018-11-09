# Install Python and dependencies
apt-get update
apt-get install python3.6
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.6

# Install Google Chrome
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >>> /etc/apt/sources.list
wget https://dl.google.com/linux/linux_signing_key.pub
apt-key add linux_signing_key.pub
apt-get update
apt-get install google-chrome-stable

# Install Docker
apt-get update
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
apt-get update
apt-get install docker-ce

# download Scraper script from S3 bucket


# Set up for scraper
docker pull fate0/headless-chrome
docker run -it --rm --cap-add=SYS_ADMIN -p9222:9222 fate0/headless-chrome &

# Run Scraper
