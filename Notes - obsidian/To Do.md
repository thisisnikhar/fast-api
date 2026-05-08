Tools Used
	|- FastAPI
	|- boto3
	|- AWS

IDE Used: Pycharm
Path: /home/nikhar-sachdeva/Desktop/path-forward/AWS-App

We will use git and branching
	|- 2 branches
		|- ec2 and s3

Folder structure
	|- 3 modules
		|- main
		|- ec2
		|- s3

We will create REST APIs to 
    |- 1. POST /ec2/instance: launch EC2 instances using a template
    |- 2. GET /ec2/running: check all the running EC2 instances
    |- 3. DELETE /ec2/<instanceId>: Terminating the instance by using the instance id
    |- 4. DELETE /ec2/: Terminate all teh instances
    |- 5. GET /ec2/<instanceid>: Get the status of EC2 instance for the given instance id
    |- 6. POST /s3/<bucket_name>: Uploads a file on the S3 bucket
    |- 7. Get /s3: Lists all the buckets
    |- 8. GET /s3/<bucket_name>: List all the files on the S3 bucket with their names
    |- 9. GET /s3/<bucket_name>/<filename>: Returns the file from S3 bucket with filename
    |- 9. DELETE /s3/<bucket_name>/<filename>: Deletes a file from S3 bucket with filename
    |- 10. GET /s3/file/<filename>: Finds the file in all the buckets and returns the bucket name with the filepath

Plan
	| - 1. main
			|- Run the application and include all the routes
	|- 2. s3
			|- On branch s3
			|- Work on this module first
	|- 3. ec2
			|- On branch ec2
			|- Work on this module second

