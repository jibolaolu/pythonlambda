import boto3

sessions = boto3.session.Session(profile_name="default")

#Resource Object
'''s3_obj_res = sessions.resource(service_name="s3")
bucket_name = "seunadio-tfstate"
bucket_object =s3_obj_res.Bucket(bucket_name)

for each_obj in bucket_object.objects.all():
    print(each_obj.key)'''

#Client Object
'''count =1
bucket_name = "seunadio-tfstate"
s3_cli_obj = sessions.client(service_name="s3")
for s3_obj in s3_cli_obj.list_objects(Bucket = bucket_name)['Contents']:
    print(count, s3_obj['Key'])
    count +=1'''

#Paginator
count =1
bucket_name = "seunadio-tfstate"
s3_cli_obj = sessions.client(service_name="s3")
paginator = s3_cli_obj.get_paginator('list_objects')
for each_obj in paginator.paginate(Bucket=bucket_name):
    for obj in each_obj['Contents']:
        print(count, obj['Key'])
        count+=1



