from pydantic import BaseModel

class RegiterUser(BaseModel):
    name:str
    email:str
    password:str

class LoginUser(BaseModel):
    email:str
    password:str