# -*- coding:UTF-8 -*-
from sqlalchemy import Column,String,Text,Integer,Varchar
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.schema import ForeignKey

# 创建对象的基类:
Base = declarative_base()

def db_connect():
    # 初始化数据库连接:
    engine = create_engine('mysql://root:ditto9689a@localhost:3306/newslistdb?charset=utf8')
    return engine

def create_table(engine):
    Base.metadata.create_all(engine)
#返回数据库会话
def loadSession(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class UserList(Base):
    __tablename='userlist'
    id=Column(Integer,primary_key=True,auto_increment)
    username=Column(String(20))
    password=Column(Varchar(20))
