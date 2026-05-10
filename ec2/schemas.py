from pydantic import BaseModel

class LaunchInstanceRequest(BaseModel):
    name:str
    launch_template:str

class TerminateInstanceRequest(BaseModel):
    name:str