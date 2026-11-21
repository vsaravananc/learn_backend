from sqlmodel import SQLModel , Field
from typing import Annotated 

class UserTable(SQLModel , table = True):
    id : Annotated[ int , Field(description="user_id",primary_key=True)]
    firstName : Annotated[ str , Field(description='User_first_name')]
    lastName : Annotated[ str , Field(description='User_last_name')]
    email : Annotated[ str , Field(description= 'User_email_id',unique=True)]
    password : Annotated[ str , Field(description='User_password')]