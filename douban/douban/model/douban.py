# -*- coding: utf-8 -*-
from sqlalchemy import Column, String , Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Douban(Base):
    __tablename__ = 'doubans'
    id = Column(Integer, primary_key=True)
   # common = Column(Integer, primary_key=True)
    pinglun = Column(String)
    #link = Column()
    #body = Column(String)
    #publish_time = Column(String)
    #source_site = Column(String)

