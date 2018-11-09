import boto3
import os

LINUX_AMI_ID = 'ami-059eeca93cf09eebd'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class EC2Controller:
    def __init__(self):
        self.state = None
        self.ec2_resource = boto3.resource('ec2')
        self.ec2_client = boto3.client('ec2')
        self.vpc = self.get_vpc()
        self.subnet = self.get_subnet()
        self.ec2 = None

    def create_instance(self):
        with open(os.path.join(ROOT_DIR, "userdata/env_setup.sh"), 'r') as f:
            user_data = f.read()
        self.ec2 = self.ec2_resource.create_instances(ImageId=LINUX_AMI_ID, InstanceType='t1.micro', MaxCount=1, MinCount=1, UserData=user_data, SubnetId=self.subnet.id)[0]

    def get_vpc(self):
        vpcs = self.ec2_client.describe_vpcs()['Vpcs']

        if len(vpcs) == 0:
            return self.ec2_resource.create_vpc(CidrBlock='10.0.0.0/16', AmazonProvidedIpv6CidrBlock=True, DryRun=False, InstanceTenancy='default')

        vpc_id = vpcs[0]['VpcId']
        return self.ec2_resource.Vpc(vpc_id)

    def get_subnet(self):
        if len(list(self.vpc.subnets.all())) == 0:
            return self.vpc.create_subnet(CidrBlock='10.0.0.0/24', DryRun=False)
        else:
            return list(self.vpc.subnets.all())[0]

    def get_instance(self, instance_id):
        self.ec2 = self.ec2_resource.Instance(instance_id)

    def delete_instance(self):
        if self.ec2 is not None:
            self.ec2.terminate(DryRun=False)
        else:
            raise Exception('EC2 Instance does not exist or set up')


