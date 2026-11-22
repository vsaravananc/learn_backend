from fastapi import FastAPI , Body , HTTPException , status
from typing import Annotated
from .model import Login , Register
from .db import Session_DB , createTable 
from .schema import UserTable
from sqlmodel import select
from pwdlib import PasswordHash
import jwt as JWT

pwdhash = PasswordHash.recommended()

PUBLIC_SECRET_KEY = '__Saravanan_Secret_Key__SSK__'
PRIVATE_SECRET_KEY = '__Saravanan_Private_Secret_key _SPSK__'

app: FastAPI = FastAPI()

@app.on_event('startup')
def on_startup():
    createTable()


@app.put('/auth/login')
def login(
    login: Annotated[Login,Body()],
    session : Session_DB
    ) -> dict:

    statement = select(UserTable).where(UserTable.email == login.email)
    result = session.exec(statement).one_or_none()

    if result is None:
        raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="User e-mail or password are wrong kindly check it")

    if not pwdhash.verify(login.password,result.password):
        raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="User e-mail or password are wrong kindly check it")
    
    encod = JWT.encode(result.model_dump(),PRIVATE_SECRET_KEY,algorithm="RS256")

    return {'message':'login sucessfully','key':encod}

@app.put('/auth/register')
def register(
    register : Annotated[Register , Body()],
    session : Session_DB
    ) -> dict:

    if register.confirmPassword != register.password:
        raise HTTPException(
            status_code= status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Entered message are not same")

    hashPassword = pwdhash.hash(register.password)
    
    user : UserTable = UserTable(
        **register.model_dump(
            exclude={'password'}
            ),
            password=hashPassword)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user.model_dump(exclude={'password'})