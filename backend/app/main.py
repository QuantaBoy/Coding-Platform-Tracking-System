from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.database import engine 
from app.models import Base

from app.routes import auth, profile, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(dashboard.router)

Base_DIR = Path(__file__).resolve().parent.parent.parent

app.mount("/static", StaticFiles(directory=str(Base_DIR/'frontend'),name = 'static'))

templates = Jinja2Templates(directory = str(Base_DIR/'frontend'/'templates'))

@app.get("/")
def home():
    return {"message": "Welcome to the Coding Platform Tracking System"}

@app.get('/login')
def login_page(request:Request):
    return templates.TemplateResponse('login.html',{"request":request})

@app.get('/register')
def register_page(request:Request):
    return templates.TemplateResponse('register.html',{"request":request})

@app.get('/complete-profile')
def complete_profile_page(request:Request):
    return templates.TemplateResponse('complete_profile.html',{"request":request})

@app.get('/profile')
def profile_page(request:Request):
    return templates.TemplateResponse('profile.html',{"request":request})
    
@app.get('/dashboard')
def dashboard_page(request:Request):
    return templates.TemplateResponse('dashboard.html',{"request":request})