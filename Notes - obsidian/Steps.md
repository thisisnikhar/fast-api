1. Create a PyCharm Project
Path: /home/nikhar-sachdeva/Desktop/path-forward/AWS-App/
And, create a virtual environment
![[Screenshot From 2026-05-08 06-11-15.png]]

2. Create a initial 'requirements.txt' file. we will add dependencies as required
* fastapi
* boto3

	**requirements.txt**
	```
	fastapi[standard]
	boto3
	```

3. Install all the dependencies using 'requirements.txt'
![[Screenshot From 2026-05-08 06-14-58.png]]

4. Initialize git repo in local using 'git init'
![[Screenshot From 2026-05-08 06-17-43.png]]

5. Create the folder structure
Folder structure
	|- 3 modules
		|- main
		|- ec2
		|- s3

![[Screenshot From 2026-05-08 06-24-11.png]]

6. AWS CLI has been already setup
![[Screenshot From 2026-05-08 06-26-28.png]]

7. Creating a branch for s3
![[Screenshot From 2026-05-08 06-29-59.png]]

8. Working on s3 service
Login to IAM User: https://aws-nikhar-v3.signin.aws.amazon.com/console
Alex; Alex@123

9. Testing the route
**main.py**
```
from fastapi import FastAPI
from s3.routes import router

app = FastAPI()

app.include_router(router)

```

**s3/routes.py**
```
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {"message": "Home Page"}
```

**Output**
![[Screenshot From 2026-05-08 06-44-11.png]]

**s3/service.py**
```
import boto3

s3 = boto3.client("s3")

def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        return "success","Bucket created successfully"
    except Exception as e:
        return "error","Error while creating a bucket"


```

#### Accessing Fast API Swagger
We can access the Swagger for FastAPI by going to: http://127.0.0.1:8000/docs
![[Screenshot From 2026-05-08 06-53-33.png]]
# Step 1: Create bucket route

10. Defining request format for create_bucket
**s3/schemas.py**
```
from pydantic import BaseModel

class CreateBucketRequest(BaseModel):
    name:str
    
```
10. Create a route to "create a bucket"
It will take bucket name as input in json
Now, our swagger API is also working
![[Screenshot From 2026-05-08 06-55-30.png]]

![[Screenshot From 2026-05-08 06-56-02.png]]

### Using schema in routes
**s3/routes.py**
```
from fastapi import APIRouter
from s3.schemas import CreateBucketRequest

from s3.service import create_bucket
router = APIRouter()


@router.get("/")
async def home():
    return {"message": "Home Page"}


@router.post("/bucket")
async def create_bucket(payload:CreateBucketRequest):
    bucket_name = payload.name
    status, message = await create_bucket(bucket_name)
    response = {
        "status": status,
        "message": message
    }
    return response
```

**s3/service.py**
```
import boto3

s3 = boto3.client("s3")

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


```

**Input**
![[Screenshot From 2026-05-08 07-18-26.png]]

**Output**
![[Screenshot From 2026-05-08 07-19-06.png]]
**Verification**
![[Screenshot From 2026-05-08 07-19-44.png]]
**Note: Deleting the bucket to ensure no cost**

# Step 2: Setting up github
1. Generate a key
![[Screenshot From 2026-05-08 07-25-56.png]]
Key Generated, fetch the public key
![[Screenshot From 2026-05-08 07-30-03.png]]


2. Start SSH agent and add your key to it
![[Screenshot From 2026-05-08 07-27-30.png]]

3. Add your key to github
![[Screenshot From 2026-05-08 07-31-10.png]]

4. Configure username and email with git
![[Screenshot From 2026-05-08 07-32-45.png]]

5. Commit the change
![[Screenshot From 2026-05-08 07-33-21.png]]
6. Create a github repo 
![[Screenshot From 2026-05-08 07-34-33.png]]
Add it to local git
![[Pasted image 20260508073519.png|697]]

7. Push the code

# Step 2: Delete Bucket Service
**s3/routes.py**
```
from fastapi import APIRouter
from s3.schemas import CreateBucketRequest

from s3.service import create_bucket_service,delete_bucket_service
router = APIRouter()


@router.get("/")
async def home():
    return {"message": "Home Page"}


@router.post("/bucket")
async def create_bucket(payload:CreateBucketRequest):
    bucket_name = payload.name
    status, message = create_bucket_service(bucket_name)
    response = {
        "status": status,
        "message": message
    }
    return response


@router.delete("/bucket")
async def remove_all_bucket():
    status, message = delete_bucket_service()
    response = {
        "status": status,
        "message": message
    }
    return response
```

**s3/service.py**
```
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
```

![[Screenshot From 2026-05-08 08-09-46.png]]
# Step 3: Push the code to github
![[Screenshot From 2026-05-08 08-11-37.png]]

