import boto3
import csv
import time
aws_con_mag = boto3.session.Session(profile_name='default')
ec2_con_res = aws_con_mag.resource(service_name='ec2')
ec2_cli = aws_con_mag.client(service_name='ec2')
count = 1
csv_obj = open("ec2_inv_info.csv","w", newline = '')
csv_wrte = csv.writer(csv_obj)
csv_wrte.writerow(["S_NO", "Instance_Id", "Instance_Type", "Architecture", "LaunchTime"])

for each_instance in ec2_con_res.instances.all():
    print(count ,each_instance, each_instance.instance_id, each_instance.instance_type, each_instance.architecture,  each_instance.launch_time.strftime("%y-%m-%d"))
    csv_wrte.writerow([count ,each_instance.instance_id, each_instance.instance_type, each_instance.architecture,  each_instance.launch_time.strftime("%y-%m-%d")])
    count +=1

csv_obj.close()
