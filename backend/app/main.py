from fastapi import FastAPI 
from app.models import Base
from app.database import engine 

Base.metadata.create_all(bind=engine)
 
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Coding Platform Tracking System"}