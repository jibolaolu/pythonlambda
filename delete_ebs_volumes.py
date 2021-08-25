import boto3
from pprint import pprint

aws_mag_con = boto3.session.Session(profile_name= 'default')
ec2_con_res = aws_mag_con.resource(service_name= 'ec2')
ec2_con_cli = aws_mag_con.client(service_name='ec2')

#Resource Object
#ec2_volume = []
'''ebs_vol = {"Name":"status", "Values": ["in-use"]}
for each_vol in ec2_con_res.volumes.filter(Filters = [ebs_vol]):
    if not each_vol.tags:
        print(each_vol.id, each_vol.state, each_vol.tags)
        print("Deleting unused and untagged Volumes")
        each_vol.delete()
print("deleted unused and untagged Volumes")
#print(ec2_volume)
#print(ec2_con_res.volumes.all())'''

#Using Client Object
#pprint(ec2_con_cli.describe_volumes()['Volumes'])
for each_volume in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_volume and each_volume['State'] == 'available':
        print(f"Deleting the Volumes {each_volume['VolumeId']}")
        ec2_con_cli.delete_volume(VolumeId=each_volume['VolumeId'])
print("Deleted unused and untagged Volumes ")