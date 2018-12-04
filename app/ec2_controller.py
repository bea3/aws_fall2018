import boto3
import os
import yaml
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class EC2Controller:
    def __init__(self):
        self.state = None
        self.ec2_resource = None
        self.ec2_client = None
        self.vpc = None
        self.subnet = None
        self.ec2 = None

        with open("config.yml", 'r') as f:
            try:
                self.config = yaml.load(f)
            except yaml.YAMLError:
                pass

    def create_instance(self, target_url=None, region=None):
        if region is None:
            region = self.config['REGION_NAME']

        self.ec2_resource = boto3.resource('ec2', region_name=region)
        self.ec2_client = boto3.client('ec2', region_name=region)
        self.vpc = self.get_vpc()
        self.subnet = self.get_subnet()
        with open(os.path.join(ROOT_DIR, "userdata/env_setup.sh"), 'r') as f:
            user_data = f.read()
            if target_url is not None:
                user_data = user_data.replace("THISISTHETARGETURL", target_url)
            user_data = user_data.replace("THISISTHEAWSKEY", self.config['AWS_ACCESS_KEY'])
            user_data = user_data.replace("THISISTHESECRETKEY", self.config['AWS_SECRET_KEY'])
        self.ec2 = self.ec2_resource.create_instances(ImageId=self.config['LINUX_AMI_ID'], InstanceType='t1.micro', MaxCount=1, MinCount=1, UserData=user_data, SubnetId=self.subnet.id, KeyName=self.config['KEY_NAME'])[0]

    def get_vpc(self):
        vpcs = self.ec2_client.describe_vpcs()['Vpcs']
        vpc_id = None

        for vpc in vpcs:
            if vpc['IsDefault']:
                vpc_id = vpc['VpcId']
                break

        if len(vpcs) == 0 or vpc_id is None:
            return self.ec2_resource.create_vpc(CidrBlock='172.31.0.0/16', AmazonProvidedIpv6CidrBlock=True, DryRun=False, InstanceTenancy='default')

        return self.ec2_resource.Vpc(vpc_id)

    def get_subnet(self):
        if len(list(self.vpc.subnets.all())) == 0:
            return self.vpc.create_subnet(CidrBlock='172.31.80.0/20', DryRun=False)
        else:
            return list(self.vpc.subnets.all())[0]

    def get_instance(self, instance_id):
        self.ec2 = self.ec2_resource.Instance(instance_id)

    def delete_instance(self):
        if self.ec2 is not None:
            self.ec2.terminate(DryRun=False)
        else:
            raise Exception('EC2 Instance does not exist or set up')


