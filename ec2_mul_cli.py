import boto3
import sys

aws_man_cli = boto3.session.Session(profile_name='default')
ec2_cli = aws_man_cli.client(service_name='ec2')

while True:
    print("This script is used for actions on ec2")
    print("""
        1. start
        2. stop
        3. terminate
        4. exit """)
    optn = int(input("Pick on of the following options: "))
    if optn == 1:
        instance_id = input("Enter your Instance Id: ")
        print(f"Starting the instance {instance_id}")
        ec2_cli.start_instances(InstanceIds = [instance_id])
    elif optn == 2:
        instance_id = input("Enter your instance Id: ")
        print(f"Stopping the instance {instance_id}")
        ec2_cli.stop_instances(InstanceIds = [instance_id])
    elif optn == 3:
        instance_id = input("Enter your instance Id: ")
        print(f"Terminating instance {instance_id}")
        ec2_cli.terminate_instances(InstanceIds = [instance_id])
    elif optn == 4:
        sys.exit()
    else:
        print("You've enter a wrong choice Please try again")