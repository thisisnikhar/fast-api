import boto3
from jinja2.bccache import Bucket
from zoneinfo import ZoneInfo

s3 = boto3.client("s3")
s3_resource = boto3.resource("s3")

def create_bucket_service(bucket_name):
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": "ap-south-1"
            }
        )
        return "success","Bucket created successfully"
    except Exception as e:
        return "error",e.args[0]


def delete_bucket_service():
    try:
        response = s3.list_buckets() # Get all the buckets
        for bucket in response["Buckets"]:
            name = bucket["Name"]
            bucket = s3_resource.Bucket(name)

            # Empty the bucket
            bucket.objects.all().delete()

            # Delete the bucket
            bucket.delete()
        return "success","Buckets deleted successfully"
    except Exception as e:
        print(e)
        return "error","Error while deleting the buckets"


def get_all_buckets_service():
    try:
        response = s3.list_buckets() # Get all the buckets
        bucket_list = []
        for bucket in response["Buckets"]:
            name = bucket["Name"]
            bucket_list.append(name)
        return "success",bucket_list
    except Exception as e:
        print(e)
        return "error","Error while fetching the bucket list"


def delete_specific_bucket_service(bucket_name):
    try:
        bucket = s3_resource.Bucket(bucket_name)
        # Empty the bucket
        bucket.objects.all().delete()

        # Delete the bucket
        bucket.delete()

        return "success",f"Bucket {bucket_name} deleted successfully"
    except Exception as e:
        print(e)
        return "error",f"Error while deleting the bucket - {bucket_name}"


def get_bucket_details_service(bucket_name):
    try:
        bucket = s3_resource.Bucket(bucket_name)
        print("-"*100)
        print(bucket)
        created_on_utc = bucket.creation_date
        # Converting time zone from utc to India
        created_on_mumbai = created_on_utc.astimezone(
            ZoneInfo("Asia/Kolkata")
        )
        created_on = created_on_mumbai.isoformat()
        region = s3.get_bucket_location(Bucket=bucket_name).get("LocationConstraint")
        # print(f"location: {location}, created_at: {created_at}")
        # return "success","test"
        print(created_on, region)
        # return  "success",""
        data = {
            "name": bucket_name,
            "created_on": created_on,
            "region": region,
        }
        return "success",data
    except Exception as e:
        print(e)
        return "error", f"Error while fetching the bucket details - {bucket_name}"