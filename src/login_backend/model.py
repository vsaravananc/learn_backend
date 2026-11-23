from typing import Annotated 
from pydantic import Field , BaseModel , EmailStr

class CreateRole(BaseModel):
    role : Annotated[str,Field(description='role')]

class Register(BaseModel):
    first_name : Annotated[str,Field(description='User_first_name')]
    last_name : Annotated[str,Field(description='User_last_name')]
    email : Annotated[EmailStr , Field(description='User_mail_id')]
    mobile_number : Annotated[str, Field(description='User_mobile_number',min_length=13,max_length=13)]
    confirm_password : Annotated[str,Field(description='User_confirm_password')]
    password :  Annotated[str,Field(description='User_password')]

class Login(BaseModel):
    email : Annotated[EmailStr , Field(description='User_mail_id')]
    password :  Annotated[str,Field(description='User_password')]

class TodoBody(BaseModel):
    title : Annotated[str,Field(default="Todo 1",min_length=3,max_length=100)]
    description : Annotated[str,Field(default="Todo 1 description",min_length=3,max_length=500)]
    completed : Annotated[bool,Field(default=False)]
