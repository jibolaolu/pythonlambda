import boto3
from pprint import pprint
import time

aws_con_mag = boto3.session.Session(profile_name='default')
ec2_res = aws_con_mag.resource(service_name='ec2')

ec2_instance = ec2_res.Instance('i-0508673aff93df1b4')
#pprint(dir(ec2_instance.state))
print("Starting the instance!! ")
ec2_instance.start()
ec2_instance.wait_until_running()
print("Your instance is up and running")




'''while True:
    ec2_instance = ec2_res.Instance('i-0508673aff93df1b4')
    print(f"The current status of ec2 is: {ec2_instance.state['Name']}")
    if ec2_instance.state['Name'] == "running":
        break
    print("Waiting to get running status .... ")
    time.sleep(10)
print("Your instance is up and running ")'''