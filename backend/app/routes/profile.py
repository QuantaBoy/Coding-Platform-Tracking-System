from fastapi import APIRouter 
from app.database import SessionLocal 
from app.models import CompleteProfile
from app.schemas import CompleteProfile

router = APIRouter()

@router.post("/completeprofile")
def complete_profile(profile:CompleteProfile):
    db = SessionLocal()
    
    new_profile = CompleteProfile(
        user_id = CompleteProfile.user_id,
        leetcode_username = CompleteProfile.leetcode_username,
        codeforces_username = CompleteProfile.codeforces_username,
        hackerrank_username = CompleteProfile.hackerrank_username,
        github_username = CompleteProfile.github_username
    )

    db.add(new_profile)
    db.commit()
    db.close()

    return {"message":"Profile Completed Successfully"}