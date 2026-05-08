import boto3

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
        print(e)
        return "error","Error while creating a bucket"


def delete_bucket_service():
    try:
        response = s3.list_buckets() # Get all the buckets
        for bucket in response["Buckets"]:
            name = bucket["Name"]
            # Empty the bucket
            bucket = s3_resource.Bucket(name)
            bucket.delete() # Deletes the bucket
        return "success","Buckets deleted successfully"
    except Exception as e:
        print(e)
        return "error","Error while deleting the buckets"