from fastapi import FastAPI , Body , HTTPException , status
from typing import Annotated
from .db import create_db_and_tables , Session_dp 
from .model import CreateRole , Register , Login
from .schema import Role , User
from pwdlib import PasswordHash
from sqlmodel import select
import jwt

pwdhash = PasswordHash.recommended()
app : FastAPI = FastAPI()

SECRET_KEY = '__SCRET_KEY__$HASH'


@app.on_event('startup')
def create_database():
    create_db_and_tables()

@app.post('/create/role',tags=['Create Role'])
def create_role(role : Annotated[CreateRole , Body()], session : Session_dp):
    insert_role : Role = Role(**role.model_dump())
    session.add(insert_role)
    session.commit()
    session.refresh(insert_role)
    return {'message':'Succesfully created role','role': role.role}

@app.post('/auth/register',tags=['Auth'])
def auth_register(register : Annotated[Register,Body()] , session : Session_dp):
    if register.confirm_password != register.password:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT,'Confirm password is not the same to password')
    encode_password = pwdhash.hash(register.password)
    user : User = User(**register.model_dump(exclude={'password'}),password=encode_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {'message':'Sucessfully create a user'}
@app.post('/auth/login',tags=['Auth'])
def auth_login(login: Annotated[Login,Body()],session : Session_dp):

    statement = select(User).where(User.email == login.email)
    result : User | None = session.exec(statement).one_or_none()
    if result is None :
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,'Email or password not correct')
    if not pwdhash.verify(login.password , result.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,'Email or password not correct')
    
    token = jwt.encode(result.model_dump(exclude={'password'}),SECRET_KEY,algorithm='HS256')
    return {'message':'login successfully','token': token} 