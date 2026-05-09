import ast

from fastapi import APIRouter
from s3.schemas import CreateBucketRequest

from s3.service import create_bucket_service,delete_bucket_service,get_all_buckets_service,delete_specific_bucket_service
from fastapi.responses import JSONResponse
router = APIRouter()


@router.get("/")
async def home():
    content = {
        "status": "success"
    }
    return JSONResponse(status_code=200,content=content)


@router.post("/bucket")
async def create_bucket(payload:CreateBucketRequest):
    bucket_name = payload.name
    status, message = create_bucket_service(bucket_name)
    content = {
        "status": status,
        "message": message
    }
    if status != "error":
        return JSONResponse(status_code=201,content=content)
    else:
        return JSONResponse(status_code=500,content=content)


@router.delete("/bucket")
async def remove_all_bucket():
    status, message = delete_bucket_service()
    content = {
        "status": status,
        "message": message
    }
    return JSONResponse(status_code=200,content=content)


@router.delete("/bucket/{bucket_name}")
async def delete_specific_bucket(bucket_name: str):
    status,message = delete_specific_bucket_service(bucket_name)
    content = {
        "status": status,
        "message": message
    }
    if status != "error":
        return JSONResponse(status_code=200,content=content)
    else:
        return JSONResponse(status_code=500,content=content)


@router.get("/bucket")
async def get_all_buckets():
    status, message = get_all_buckets_service()
    content = {
        "status": status,
        "message": message
    }
    return JSONResponse(status_code=200,content=content)