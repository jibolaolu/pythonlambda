import boto3

session= boto3.session.Session(profile_name="default")
ec2_instance = session.resource(service_name='ec2')
sns_cli = session.client(service_name='sns')

my_instance = ec2_instance.Instance('i-0bc5cd72e1277d0e6')
print(my_instance.state['Name'])

sns_cli.publish(TargetArn="arn:aws:sns:eu-west-2:100753669199:ec2_mail",Message=my_instance.state['Name'])