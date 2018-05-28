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
# for simplification dont create a table, but use this json as mocked table
Rootdescription = {
                'App': 'Proxy API!',
                'Version' : '0.3',
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)),
                 'possible_routes' : {
                        'Box' : '/boxes/, /boxes/<int:box-id>',
                        'Address' : '/addresses/, /addresses/<int:box-id>',
                     'Content': '/contents/, /contents/<int:content-id>'}
                 }


class Content(Base):
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    box_id = Column(Integer, ForeignKey('box.id'))

    style = Column(String(50))
    color = Column(String(50))
    size = Column(String(3))
    price = Column(String(10))
    condition = Column(String(20))




class Address(Base):

     __tablename__ = 'address'
     id = Column(Integer, primary_key=True)
     name = Column(String(100))
     str_name = Column(String(50))
     str_no = Column(String(10))
     city = Column(String(30))
     state = Column(String(50))
     post_code = Column(String(10))
     country = Column(String(50))
     start_date = Column(DateTime, default=datetime.datetime.utcnow)
     end_date = Column(DateTime, default=datetime.datetime.utcnow)



class Box(Base):
    __tablename__ = 'box'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    # one box has a current address
    addr_c_id = Column(Integer, ForeignKey('address.id'))
    addr_c = relationship(Address,foreign_keys=[addr_c_id], lazy='joined')

    # one box has a destination address
    addr_d_id = Column(Integer, ForeignKey('address.id'))
    addr_d = relationship(Address, foreign_keys=[addr_d_id], lazy = 'joined')

    # one box has a product
    #box_content_id = Column(Integer, ForeignKey('content.id'))
    box_contents = relationship('Content', lazy = 'joined')

    status = Column(String(50))
    customerStatus = Column(String(50))
    weight = Column(String(10))
    size = Column(String(10))








        

    
    
    