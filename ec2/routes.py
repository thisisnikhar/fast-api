from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ec2.service import get_instances_service, launch_instance_service
from ec2.schemas import LaunchInstanceRequest

router = APIRouter()


@router.get("/instances")
async def get_instances():
    status, message = get_instances_service()
    content = {
        "status": status,
        "message": message
    }
    return JSONResponse(status_code=200,content=content)


@router.post("/instances")
async def launch_instance(payload: LaunchInstanceRequest):
    instance_name = payload.name
    launch_template= payload.launch_template
    status, message = launch_instance_service(instance_name,launch_template)
    content = {
        "status": status,
        "message": message
    }
    if status != "error":
        return JSONResponse(status_code=201, content=content)
    else:
        return JSONResponse(status_code=500, content=content)