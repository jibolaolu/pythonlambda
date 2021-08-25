import boto3
from pprint import pprint
import datetime

session = boto3.session.Session(profile_name='default')
aws_res = session.resource(service_name='iam')

count = 1
#iam_user_obj = aws_res.users.all()
for iam_user in aws_res.users.all():
    #print(count, iam_user.name)
    print(count, iam_user.user_id, iam_user.user_name, iam_user.arn, iam_user.create_date.strftime("%Y-%M-%d"))
    count +=1
#print(iam_user_obj)
#iam_usr = aws_res.User('oluseun')
#print(iam_usr.user_id, iam_usr.user_name, iam_usr.arn, iam_usr.create_date.strftime("%Y-%M-%d"))
