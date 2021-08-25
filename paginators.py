import boto3
from pprint import pprint

session = boto3.session.Session(profile_name="default")
'''ec2_res = session.resource(service_name="iam")
count = 1
for each_user in ec2_res.users.all():
    print(each_user.user_name)
    count +=1

#Client
count = 1
iam_cli = session.client(service_name="iam")
#print(iam_cli.list_users())
for each_user in iam_cli.list_users()['Users']:
    print(count, each_user['UserName'])
    count+=1'''
'''iam_cli = session.client(service_name="iam")

paginator = iam_cli.get_paginator('list_users')
for each_page in paginator.paginate():
    for each_user in each_page['Users']:
        print(each_user['UserName'])'''

iam_cli = session.client(service_name="ec2")
paginator = iam_cli.get_paginator('describe_instances')
for each_instance in paginator.paginate():
    for each_instnce in each_instance['Reservations']:
        for instance_id in each_instnce['Instances']:
            print(instance_id['InstanceId'])

    #print(each_instance)