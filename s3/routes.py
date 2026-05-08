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