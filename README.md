### Set Up ###
You need to create a credential file. The default location is `~/.aws/credentials` for Unix/Linux.
Replace the AWS Key and AWS Secret Key in app/userdata/env_setup.sh
Security Group for EC2 Instance should have Inbound Rule for SSH TCP 22 to 0.0.0.0/0

### To Do ###
* Read Config file and use that instead of hardcoding things
* Send request body using lambda controller
* EC2 Instance User data scrapes data
