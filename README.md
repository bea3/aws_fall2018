# AWS Scraper #
This system allows you to create an EC2 instance, scrape a website, and send the website elements back to an S3 Bucket.

### Pre-Requisites ###
* Python3.4 or newer
* AWS Credentials

### Set Up ###
1. Create an AWS credential file on your host machine. The default location is `~/.aws/credentials` for Unix/Linux.
Replace the AWS_ACCESS_KEY and AWS_SECRET_KEY in config.yml
2. Create a Keypair that will be used for the EC2 Instances. Replace KEY_NAME with the name of your keypair.
3. Security Group for EC2 Instance should have Inbound Rule for SSH TCP 22 to 0.0.0.0/0 and set it as a Default Security group. Future development of this project will create a security group with these inbound rules if it has not been created already.
4. Create an S3 bucket called website-elements.

### To Do ###
* Send request body using lambda controller
* EC2 Instance User data scrapes data
