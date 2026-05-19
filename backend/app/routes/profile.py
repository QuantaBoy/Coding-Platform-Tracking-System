from fastapi import APIRouter 
from ..database import SessionLocal 
from ..models import CompleteProfile
from ..schemas import CompProfile

router = APIRouter()

@router.post("/completeprofile")
def complete_profile(profile:CompProfile):
    db = SessionLocal()
    
    new_profile = CompleteProfile(
        roll_number = profile.roll_number,
        leetcode_username = profile.leetcode_username,
        codeforces_username = profile.codeforces_username,
        hackerrank_username = profile.hackerrank_username,
        github_username = profile.github_username
    )

    db.add(new_profile)
    db.commit()
    db.close()

    return {"message":"Profile Completed Successfully"}

@router.get("/profile/{roll_number}")
def get_profile(roll_number : str):
    db = SessionLocal()

    profile = db.query(CompleteProfile).filter(CompleteProfile.roll_number == roll_number).first()

    db.close()

    if not profile:
        return {"message":"Profile not found"}

    return {
        "leetcode_username" : profile.leetcode_username,
        "codeforces_username":profile.codeforces_username,
        "hackerrank_username":profile.hackerrank_username,
        "github_username":profile.github_username
    }