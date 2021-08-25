#!/usr/bin/python3
import boto3
from pprint import pprint

aws_s3 = boto3.session.Session(profile_name= 'default')
s3_cli = aws_s3.client(service_name="s3")
lst_s3 = aws_s3.resource('s3')

'''for s3_buucket in lst_s3.buckets.all():
    print(s3_buucket.name)'''

for each_s3 in s3_cli.list_buckets()['Buckets']:
    print(each_s3['Name'])
