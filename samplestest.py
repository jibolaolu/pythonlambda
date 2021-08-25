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
    pmry_netwrk_intface = primary_instance.network_interfaces_attribute[0]
    scdry_netwrk_intface = secondary_instance.network_interfaces_attribute[0]
    pnwk_interface_id = pmry_netwrk_intface['NetworkInterfaceId']
    snwk_interface_id = pmry_netwrk_intface['NetworkInterfaceId']
    #print(dir(pmry_netwrk_intface))
    ec2_cli = session.client(service_name="ec2")
    ec2_cli.unassign_private_ip_addresses(
        NetworkInterfaceId= pnwk_interface_id,
        PrivateIpAddresses=[secondary_ip]
    )
    ec2_cli.assign_private_ip_addresses(
        AllowReassignment=True,
        NetworkInterfaceId=snwk_interface_id ,
        PrivateIpAddresses = [secondary_ip]
    )
