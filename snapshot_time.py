import boto3
import datetime
from pprint import pprint

aws_con_mag = boto3.session.Session(profile_name='default')
ec2_con_res = aws_con_mag.resource(service_name='ec2', region_name='eu-west-2')
aws_acct_id = aws_con_mag.client(service_name='sts')
ec2_cli = aws_con_mag.client(service_name='ec2')

today = datetime.datetime.now()
start_time = str(datetime.datetime(today.year, today.month, today.day))
#get caller ID
caller_id = aws_acct_id.get_caller_identity()
resp = caller_id.get('Account')

count = 1
for snapshot in ec2_con_res.snapshots.filter(OwnerIds=[resp]):
    if snapshot.start_time.strftime("%Y-%m-%d %H:%M:%S") == start_time:
        print(count, snapshot.id, snapshot.start_time.strftime("%Y-%m-%d %H:%M:%S"))
        count+=1
