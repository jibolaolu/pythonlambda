import boto3

aws_mag_cons = boto3.session.Session(profile_name='default')
sts_con = aws_mag_cons.client(service_name='sts')
response = sts_con.get_caller_identity()['Account']

print(response)
