# Install Python and dependencies
apt-get update
apt-get install -y python3
apt-get install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get update -y
apt-get install -y python-dev build-essential
python -m pip install pip==9.0.3

# Install AWS CLI
python -m pip install awscli --upgrade --user

# Create Credentials file for AWS
mkdir .aws
echo "
[default]
aws_access_key_id = AKIAIYGBHONRPVFMU3FQ
aws_secret_access_key = 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" >> ~/.aws/credentials

# Download Scraper script from S3 bucket
aws s3 cp s3://scrape-fall2018/scraper.py .

# Download requirements.txt from S3 bucket
aws s3 cp s3://scrape-fall2018/requirements.txt .
python -m pip install -r requirements.txt

# Install Google Chrome
apt-get install -y libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome*.deb

# Set up Pychrome
python -m pip install -U pychrome
google-chrome --headless --disable-gpu --remote-debugging-port=9222 &

# Run Scraper
REPLACE IP ADDRESS IN SCRAPER WITH IP ADDRESS OF EC2 INSTNACE
python scraper.py
