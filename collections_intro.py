import boto3

aws_mag_cons = boto3.session.Session(profile_name='default')
ec2_cons = aws_mag_cons.resource(service_name='ec2')
#print(ec2_cons.instances.all())
f1 = {"Name": "instance-state-name", "Values": ["stopped"]}
f2 = {"Name": "instance-type", "Values": ["t2.micro"]}
for each_ec2 in ec2_cons.instances.filter(Filters = [f1,f2]):
    print(each_ec2)
