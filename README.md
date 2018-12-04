# Bot Scraper #
This system automates the process of scraping a website. The objective is that a user would be able to call a POST Request to an endpoint with a request body of the target website to scrape. Then, the endpoint will trigger a lambda service, which will create an EC2 instance, use a headless chrome browser to scrape the website, and return that data back to an S3 bucket.
The file "architecture.png" in this directory shows the goal architecture of this system.

### Resources Used ###
During the course of this project, I used several types of AWS technologies including:
* Amazon API Gateway
* AWS Lambda Service
* Python's Boto3
* AWS cli commands
* EC2 Instance's user data

### Set Up ###
1. Create a credential file. The default location is `~/.aws/credentials` for Unix/Linux.
2. Create an AWS Key and AWS Secret Key
3. Create a keypair that would be used for the EC2 instances.
4. Replace the AWS Key, AWS Secret Key, and Key Pair name in configuration.yml with your information.
5. Create a Security Group for EC2 Instances. It should have Inbound Rule for SSH TCP 22 to 0.0.0.0/0
6. Set up an AWS API Gateway to take in a POST request
    1. Log in to the AWS Console Page and go to the Amazon API Gateway service
    2. Click on "Create API"
    3. 

### Future Work ###
In the future, the main objective would be include the capability of EC2 instances to terminate themselves after they are done scraping and sending data to the S3 bucket.
Other improvements include, automating the Set Up process as much as possible.

### Resources ###

### To Do ###
* Send request body using lambda controller
