from fastapi import APIRouter
from app.database import SessionLocal
from app.models import CompleteProfile
from app.services.code_forces import get_user_info, get_rating_history, get_submission

router = APIRouter()

@router.get("/dashboard/{username}")

def get_dashboard(user_id :int):

    db = SessionLocal()
    