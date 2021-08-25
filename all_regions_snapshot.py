import boto3
session = boto3.session.Session(profile_name="default")
ec2_cli = session.client(service_name="ec2")

all_regions = []
for each_regions in ec2_cli.describe_regions()['Regions']:
    all_regions.append(each_regions['RegionName'])

for each_rgn in all_regions:
    print(f"I'm currently working on region {each_rgn}")
    ec2_cli = session.client(service_name="ec2", region_name=each_rgn)
    lst_vol_ids = []
    fil_volume = {"Name":"tag:Env", "Values": ["Prod"]}
    paginator = ec2_cli.get_paginator('describe_volumes')
    for each_pag in paginator.paginate(Filters = [fil_volume]):
        for each_vol in each_pag['Volumes']:
            lst_vol_ids.append(each_vol['VolumeId'])
    print(f"The list of volumes are {lst_vol_ids} ")

    #Dont take snapshots if region empty
    if bool (lst_vol_ids) == False:
        continue
    #Taking Volume-snapshots
    snapshots_ids = []
    for each_volId in lst_vol_ids:
        print(f"Taking Snapshot of {each_volId}")
        response=ec2_cli.create_snapshot(
            Description = "Taking snapshot of the Volumes ",
            VolumeId = each_volId,
            TagSpecifications = [
                {
                    "ResourceType": "snapshot",
                    "Tags": [
                        {
                            "Key": "Delete-on",
                            "Value": "90"
                        }
                    ]
                }
            ]
        )
        snapshots_ids.append(response['SnapshotId'])
    print(f"The snapshotids are {snapshots_ids}")
    waiter = ec2_cli.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapshots_ids)
    print(f"Successfully take snapshots of volume id {lst_vol_ids}")

