from sqlmodel import create_engine ,SQLModel , Session 
from typing import Annotated 
from fastapi import Depends

SQLFILE_NAME = 'user.db'
SQL_URL = f'sqlite:///{SQLFILE_NAME}'
CONNECTION_ARGS = {'check_same_thread' : False}

CREATE_ENGINE = create_engine(SQL_URL ,connect_args = CONNECTION_ARGS)

def createTable():
    SQLModel.metadata.create_all(CREATE_ENGINE)


def get_session():
    with Session(CREATE_ENGINE) as session:
        yield session

Session_DB = Annotated[ Session , Depends(get_session) ]