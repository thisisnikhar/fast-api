from pydantic import BaseModel

class CreateBucketRequest(BaseModel):
    name:str
