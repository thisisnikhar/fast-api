import boto3


ec2 = boto3.client("ec2",region_name="ap-south-1")
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


def launch_instance_service(instance_name,launch_template):
    response = ec2.run_instances(
        LaunchTemplate={
            'LaunchTemplateName': launch_template,
            'Version': '$Latest'
        },
        MinCount = 1,
        MaxCount = 1,
        # Defining the instance name below
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name  # This becomes the display name
                    },
                ]
            },
        ]
    )
    instance_id = response['Instances'][0]['InstanceId']
    return "success", instance_id