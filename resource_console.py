import boto3

aws_con = boto3.session.Session(profile_name='default')
iam_res_con = aws_con.resource(service_name= 'iam')
ec2_res_con = aws_con.resource(service_name= 'ec2')
s3_res_con = aws_con.resource(service_name= 's3')

#List all iam users

response = iam_res_con.users.all()
#print(dir(response))
for each_user in response:
    print(each_user.user_name)

#List all ec2 buckets
ec2_resp = ec2_res_con.instances.all()
for each_ec2 in ec2_resp:
    print(each_ec2.id)


#List all s3 buckets
s3_resp = s3_res_con.buckets.all()
for each_s3 in s3_resp:
    print(each_s3.name)
