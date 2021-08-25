import boto3
import sys
from pprint import pprint

aws_mang_cons = boto3.session.Session(profile_name='default')
ec2_cons_res = aws_mang_cons.resource(service_name='ec2')
ec2_cons_cli = aws_mang_cons.client(service_name='ec2')

while True:
    print("This script performs the following actions on ec2")
    print(""""
        1. start
        2. stop
        3. terminate
        4. exit       
        """)
    opt = int(input("Enter your option from 1-4: "))
    if opt == 1:
        instance_id = input("Enter your instance id: ")
        my_instance = ec2_cons_res.Instance(instance_id)
        print(f"Starting ec2 instance {instance_id}")
        my_instance.start()
    elif opt == 2:
        instance_id = input("Enter your instance id: ")
        my_instance = ec2_cons_res.Instance(instance_id)
        print(f"Stopping ec2 Instance {instance_id}")
        my_instance.stop()
    elif opt == 3:
        instance_id = input("Enter your instance id: ")
        my_instance = ec2_cons_res.Instance(instance_id)
        print(f"Terminating ec2 Instance {instance_id}")
        my_instance.terminate()
    elif opt == 4:
        print("Thanks for using this script")
        sys.exit()
    else:
        print("You've selected an invalid option!! ")

