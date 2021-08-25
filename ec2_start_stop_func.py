import json
import boto3

def lambda_handler(event, context):
    ec2_con_res = boto3.resource(service_name="ec2", region_name="eu-west-2")
    env_filter = {"Name":"tag:Env", "Values":["Test"]}
    for each_instance in ec2_con_res.instances.filter(Filters=[env_filter]):
        each_instance.start()
        print(each_instance.id)
    return "Success"