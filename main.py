from fastapi import FastAPI
from s3.routes import router

app = FastAPI()

app.include_router(router)