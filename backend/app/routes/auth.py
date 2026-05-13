from fastapi import APIRouter
from ..models import User
from ..schemas import RegisterUser,LoginUser
from ..database import SessionLocal
from ..utils import hash_password,verify_password

router = APIRouter()

@router.post("/register")
def register_user(user:RegisterUser):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.email==user.email).first()

    if(existing_user):
        return {"message":"User Already Exists"}
    
    hash_pwd = hash_password(user.password)

    new_user = User(name=user.name,email=user.email,password = hash_pwd)

    db.add(new_user)
    db.commit()
    db.close()

    return {"message":"User Registered Sucessfully"}

@router.post('/login')
def login_user(user:LoginUser):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.email==user.email).first()

    if(not existing_user):
        db.close()
        return {"message":"Need to Register First"}

    valid_pass = verify_password(user.password,existing_user.password)
    if not valid_pass:
        db.close()
        return {"message":"Incorrect Password"}
    db.close()
    return{"message":"Login Successfull", "email":existing_user.email}
        
