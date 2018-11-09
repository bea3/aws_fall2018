from app import ec2_controller

ec2_controller = ec2_controller.EC2Controller()
# ec2_controller.create_instance()
instance_id = "i-04bb875bd8b7824e5"
ec2_controller.get_instance(instance_id)
ec2_controller.delete_instance()
