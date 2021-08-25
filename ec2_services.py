import boto3
from pprint import pprint

aws_mag_cons = boto3.session.Session(profile_name='default')
ec2_serv = aws_mag_cons.client(service_name='ec2')

'''response = ec2_serv.describe_instances()['Reservations']
for each_item in response:
    for each_instance in each_item['Instances']:
        print("The Image used for the instance is: {}\nThe Instance Id is {}\nThe Instance type is {}".format(each_instance['ImageId'],
            each_instance['InstanceId'], each_instance['InstanceType']))'''

resp = ec2_serv.describe_volumes()['Volumes']
#pprint(resp)
for each_vol in resp:
    print("The Volume Id is {}\nThe Volume size is {}\nVolume was created on {}".format(each_vol['VolumeId'], each_vol['Size'],
        each_vol['CreateTime'].strftime("%Y-%m-%d")))
