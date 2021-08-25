import boto3

aws_cons = boto3.session.Session(profile_name= 'default')

iam_con_res = aws_cons.resource(service_name= 'iam', region_name= 'eu-west-2')
iam_con_cli = aws_cons.client(service_name= 'iam', region_name= 'eu-west-2')

#Listing iam users with resource object
for each_iam in iam_con_res.users.all():
    print(each_iam.name)

print("<<<<<<===================>>>>>>>>>>")

for iam_usr in iam_con_cli.list_users()['Users']:
    print(iam_usr['UserName'])