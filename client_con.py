import boto3

aws_mag = boto3.session.Session(profile_name='default')
iam_con = aws_mag.client(service_name='iam')
ec2_con = aws_mag.client(service_name='ec2')
s3_con = aws_mag.client(service_name='s3')


#List all iam_users using client object

response = iam_con.list_users()
for each_name in response['Users']:
    print(each_name['UserName'])


#List all ec2s
resp = ec2_con.describe_instances()['Reservations']
for each_itm in resp:
    for each_instance in each_itm['Instances']:
        print(f"The instance Id is {each_instance['InstanceId']}" )
        print("====================")


resp_s3 = s3_con.