import boto3
from pprint import pprint

aws_con_mag = boto3.session.Session(profile_name='default')
ec2_con_res = aws_con_mag.resource(service_name='ec2', region_name='eu-west-2')
aws_acct_id = aws_con_mag.client(service_name='sts')
ec2_cli = aws_con_mag.client(service_name='ec2')

#get caller ID
caller_id = aws_acct_id.get_caller_identity()
resp = caller_id.get('Account')
fsize= {"Name":"volume-size", "Values": ["8"]}
count = 1
for snapshot in ec2_con_res.snapshots.filter(OwnerIds=[resp],Filters=[fsize]):
    print(count, snapshot)
    count += 1
