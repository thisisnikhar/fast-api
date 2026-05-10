from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ec2.service import (get_instances_service, launch_instance_service,
                         get_instances_by_state_service,terminate_instance_by_id_service)
from ec2.schemas import LaunchInstanceRequest, TerminateInstanceRequest

router = APIRouter()


@router.get("/instances")
async def get_instances():
    status, message = get_instances_service()
    content = {
        "status": status,
        "message": message
    }
    return JSONResponse(status_code=200,content=content)


@router.get("/instances/state/{state}")
async def get_instance_by_state(state):
    status, message = get_instances_by_state_service(state)
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


@router.delete("/instances/")
async def terminate_instance(payload: TerminateInstanceRequest):
    instance_ids = payload.instance_ids
    status, message = terminate_instance_by_id_service(instance_ids)
    content = {
        "status": status,
        "message": message
    }
    if status != "error":
        return JSONResponse(status_code=200,content=content)
    else:
        return JSONResponse(status_code=500, content=content)