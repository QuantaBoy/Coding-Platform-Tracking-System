from fastapi import APIRouter
from app.database import SessionLocal
from app.models import CompleteProfile
from app.services.code_forces import get_user_info, get_rating_history, get_submission

router = APIRouter()

@router.get("/dashboard/{roll_number}")
def get_dashboard(roll_number: str):
    db = SessionLocal()
    
    profile = db.query(CompleteProfile).filter(CompleteProfile.roll_number == roll_number).first()

    db.close()

    if not profile:
        return {"message":"Profile not Found"}

    codeforces_username = profile.codeforces_username

    user_info = get_user_info(codeforces_username)
    rating_history = get_rating_history(codeforces_username)
    submissions = get_submission(codeforces_username)

    return {
        "codeforces_info" : user_info,
        "rating_history" : rating_history,
        "submissions" : submissions
    }