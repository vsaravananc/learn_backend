from typing import Annotated 
from pydantic import BaseModel , Field , EmailStr

class Login(BaseModel):
    email : Annotated[ EmailStr , Field(description= 'User_email_id')]
    password : Annotated[ str , Field(description='User_password')]

class Register(Login):
    firstName : Annotated[ str , Field(description='User_first_name')]
    lastName : Annotated[ str , Field(description='User_last_name')]
    confirmPassword : Annotated[ str , Field(description='User_confirm_password')]
