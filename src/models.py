# -*- coding: utf-8 -*-
import datetime
import os

from sqlalchemy import Column, Date, DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from src.settings import DB_URI

Base = declarative_base()
engine = create_engine(DB_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Define the current Version for api endpoint description
Rootdescription = {
                'App': 'Proxy API!',
                'Version' : '0.3',
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)),
                 'possible_routes' : {
                        'Box' : '/boxes/, /boxes/<int:box-id>',
                        'Address' : '/addresses/, /addresses/<int:box-id>'}
                 }

class Address(Base):

     __tablename__ = 'address'
     id = Column(Integer, primary_key=True)
     name = Column(String(250))
     str_name = Column(String(50))
     str_no = Column(String(10))
     city = Column(String(30))
     post_code = Column(String(10))
     country = Column(String(50))
     start_date = Column(DateTime, default=datetime.datetime.utcnow)
     end_date = Column(DateTime, default=datetime.datetime.utcnow)



class Box(Base):
    __tablename__ = 'box'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    addr_c_id = Column(Integer, ForeignKey('address.id'))
    addr_c = relationship(Address,foreign_keys=[addr_c_id], lazy='joined')
    addr_d_id = Column(Integer, ForeignKey('address.id'))
    addr_d = relationship(Address, foreign_keys=[addr_d_id], lazy = 'joined')
    status = Column(String(250))
    weight = Column(String(250))
    size = Column(String(250))






        

    
    
    