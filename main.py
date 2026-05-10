from fastapi import FastAPI
from s3.routes import router as s3_router
from ec2.routes import router as ec2_router

app = FastAPI()

app.include_router(s3_router)
app.include_router(ec2_router)