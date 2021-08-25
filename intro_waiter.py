import boto3

aws_con_mag = boto3.session.Session(profile_name='default')
ec2_cli = aws_con_mag.client(service_name='ec2')

print("Starting your ec2 instance!!")
ec2_cli.start_instances(InstanceIds =['i-0508673aff93df1b4'])
waiter = ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds =['i-0508673aff93df1b4'])
print("Your instance is up and running  ")
#print("Starting you instance !")
