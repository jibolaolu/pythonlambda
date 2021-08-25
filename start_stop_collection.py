import boto3

aws_mag_cons = boto3.session.Session(profile_name='default')
ec2_cons_res = aws_mag_cons.resource(service_name='ec2')
ec2_con_cli = aws_mag_cons.client(service_name='ec2')

'''
#To get Ids of all running instances
all_instance_id = []
for each_instance in ec2_cons_res.instances.all():
    all_instance_id.append(each_instance.id)
#Crate a waiter object using client
waiter= ec2_con_cli.get_waiter('instance_running')
print("Start all instances !! ")
ec2_cons_res.instances.start()
waiter.wait(InstanceIds = all_instance_id)
print("All  instances are up and running "
'''

#collecting particular group of servers
#Resources
'''np_serv_ids = []
f1 = {"Name":"tag:Name", "Values": ["Ubuntu_server"]}
for each_serv in ec2_cons_res.instances.filter(Filters =[f1]):
    np_serv_ids.append(each_serv.id)
    print(np_serv_ids)'''

#Using client
np_serv_ids = []
f1 = {"Name":"tag:Name", "Values": ["Ubuntu_server"]}
for each_sev in ec2_con_cli.describe_instances(Filters = [f1])['Reservations']:
    for each_in in each_sev['Instances']:
        np_serv_ids.append(each_in['InstanceId'])
print(np_serv_ids)

print(f"Starting instances of id {np_serv_ids} ")
ec2_con_cli.start_instances(InstanceIds=np_serv_ids)
waiter= ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds = np_serv_ids)
print("Instances is up and running ")
