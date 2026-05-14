from pydantic import BaseModel

class RegisterUser(BaseModel):
    name:str
    email:str
    password:str

class LoginUser(BaseModel):
    email:str
    password:str

class CompProfile(BaseModel):
    user_id:int
    leetcode_username:str
    codeforces_username:str 
    hackerrank_username:str
    github_username:str