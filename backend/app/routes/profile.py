from fastapi import APIRouter 
from ..database import SessionLocal 
from ..models import CompleteProfile
from ..schemas import CompProfile

router = APIRouter()

@router.post("/completeprofile")
def complete_profile(profile:CompProfile):
    db = SessionLocal()
    
    new_profile = CompleteProfile(
        user_id = profile.user_id,
        leetcode_username = profile.leetcode_username,
        codeforces_username = profile.codeforces_username,
        hackerrank_username = profile.hackerrank_username,
        github_username = profile.github_username
    )

    db.add(new_profile)
    db.commit()
    db.close()

    return {"message":"Profile Completed Successfully"}