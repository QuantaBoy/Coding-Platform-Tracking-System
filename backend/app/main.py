from fastapi import FastAPI 
from app.models import Base
from app.database import engine 
from app.routes import auth, profile, dashboard
Base.metadata.create_all(bind=engine)
 
app = FastAPI()

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(dashboard.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Coding Platform Tracking System"}