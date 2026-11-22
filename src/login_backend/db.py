from sqlmodel import create_engine , SQLModel , Session
from typing import Annotated 
from fastapi import Depends

SQL_FILE_NAME = 'todo.db'
SQL_PATH = f'sqlite:///{SQL_FILE_NAME}'
CONNECTION_ARGUMENT = {'check_same_thread': False}
ENGINE = create_engine(SQL_PATH,connect_args=CONNECTION_ARGUMENT)

def create_db_and_tables():
    SQLModel.metadata.create_all(ENGINE)

def create_session():
    with Session(ENGINE) as session :
        yield session

Session_dp = Annotated[ Session , Depends(create_session) ]