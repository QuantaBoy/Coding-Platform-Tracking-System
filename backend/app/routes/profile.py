from fastapi import APIRouter 
from ..database import SessionLocal 
from ..models import CompleteProfile
from ..schemas import CompProfile

router = APIRouter()

@router.post("/completeprofile")
def complete_profile(profile:CompProfile):
    db = SessionLocal()
    
    existing_profile = db.query(CompleteProfile).filter(CompleteProfile.roll_number == profile.roll_number).first()
    
    if existing_profile:
        existing_profile.leetcode_username = profile.leetcode_username
        existing_profile.codeforces_username = profile.codeforces_username
        existing_profile.hackerrank_username = profile.hackerrank_username
        existing_profile.github_username = profile.github_username
        db.commit()
        db.close()
        return {"message":"Profile Completed Successfully"}
        
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
    user = db.query(User).filter(User.roll_number == roll_number).first()

    db.close()

    if not profile:
        return {"message":"Profile not found"}

    return {
        "name": user.name if user else "",
        "email": user.email if user else "",
        "leetcode_username" : profile.leetcode_username,
        "codeforces_username":profile.codeforces_username,
        "hackerrank_username":profile.hackerrank_username,
        "github_username":profile.github_username
    }