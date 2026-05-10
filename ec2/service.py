import boto3


ec2 = boto3.client("ec2")
ec2_resource = boto3.resource("ec2",region_name="ap-south-1")


def get_instances_service():
    instance_list = []
    for instance in ec2_resource.instances.all():
        d = {
            "instance_id": instance.id,
            "instance_name":next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), 'N/A'),
            "instance_state": instance.state['Name']
        }
        instance_list.append(d)
    return "success",instance_list