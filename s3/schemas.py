from pydantic import BaseModel

class CreateBucketRequest(BaseModel):
    name:str

class DeleteBucketRequest(BaseModel):
    name:str