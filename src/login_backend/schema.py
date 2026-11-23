from sqlmodel import SQLModel , Field 
from datetime import datetime , timezone

class Role(SQLModel, table = True):
    id : int | None = Field(default=None,primary_key=True)
    role : str = Field(unique=True)
    create_at : datetime | None = Field(default=datetime.now(timezone.utc))

class User(SQLModel, table = True):
    id : int | None = Field(default=None,primary_key=True)
    first_name : str
    last_name : str
    mobile_number : str = Field(max_length=13,unique=True)
    email : str = Field(unique=True)
    password : str
    role_id : int | None = Field(foreign_key="role.id")
    created_at : datetime | None = Field(default=datetime.now(timezone.utc))

class Todo(SQLModel , table = True):
    id : int | None = Field(default= None , primary_key= True)
    title : str
    description : str
    user_id : int = Field(foreign_key='user.id')
    completed : bool = Field(default= False)
    created_at : datetime | None = Field(default=datetime.now(timezone.utc))

