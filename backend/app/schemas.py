from pydantic import BaseModel

class RegisterUser(BaseModel):
    roll_number:str
    name:str
    email:str
    password:str

class LoginUser(BaseModel):
    roll_number:str
    password:str

class CompProfile(BaseModel):
    roll_number:str
    leetcode_username:str
    codeforces_username:str 
    hackerrank_username:str
    github_username:str