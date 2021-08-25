import boto3

aws_mag_cons = boto3.session.Session(profile_name='default')
ec2_con = aws_mag_cons.client(service_name='ec2')