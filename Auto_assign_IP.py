import boto3

session = boto3.session.Session(profile_name='default')
ec2_res = session.resource(service_name='ec2')
master_id = "i-0879d4e3a43c89c7c"
slave_id  = "i-0bc5cd72e1277d0e6"
secondary_ip = "172.31.18.33"

primary_instance = ec2_res.Instance(master_id)
if primary_instance.state['Name'] == "running":
    print("Master instance is running no modification")
else:
    secondary_instance = ec2_res.Instance(slave_id)
print(primary_instance.state)
