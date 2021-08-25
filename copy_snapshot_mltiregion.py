import os, sys
try:
    import boto3
    print("Imported Boto3 Successfully")
except Exception as e:
    print(e)
    sys.exit(1)
source_region = 'eu-west-2'
dest_region = 'eu-west-1'
session = boto3.session.Session(profile_name="default")
ec2_cli = session.client(service_name="ec2", region_name=source_region)

sts_cli = session.client(service_name='sts')
account_id = sts_cli.get_caller_identity()['Account']
fil_vol_bck = {"Name": "tag:Env","Values": ["Dev"]}
backup_snap = []

#Get all snapshot
for each_snap in ec2_cli.describe_snapshots(OwnerIds=[account_id], Filters=[fil_vol_bck])['Snapshots']:
    backup_snap.append(each_snap['SnapshotId'])
print(f"The list of volumes to back up are  {backup_snap}")

#copy to another region
ec2_cli_destn = session.client(service_name='ec2', region_name=dest_region)
for snap_insource in backup_snap:
    print(f"Taking Snaps for {snap_insource} into region {dest_region}")
    ec2_cli_destn.copy_snapshot(
        Description = "Bacup for disaster recovery",
        SourceRegion = source_region,
        SourceSnapshotId = snap_insource
    )
#waiter = ec2_cli.get_waiter('snapshot_completed')
#waiter.wait(SnapshotIds=snap_insource)
print(f"Successfully copied over to {dest_region}")
print("Modifying snapshot tags")
for snap_insource in backup_snap:
    print(f"Deleting Old tags for {snap_insource}")
    ec2_cli.delete_tags(
        Resources =[snap_insource],
        Tags = [
            {"Key": "Env",
             "Value":"Dev"
             }
        ]
    )
    print(f"Creating new tags for {snap_insource}")
    ec2_cli.create_tags(
        Resources = [snap_insource],
        Tags =[
            {"Key": "Env",
             "Value": "Dev-completed"

             }]
    )