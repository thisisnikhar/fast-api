from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ec2.service import get_instances_service

router = APIRouter()


@router.get("/instances")
async def get_instances():
    status, message = get_instances_service()
    content = {
        "status": status,
        "message": message
    }
    return JSONResponse(status_code=200,content=content)