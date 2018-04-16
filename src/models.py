# -*- coding: utf-8 -*-
import datetime

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




def init_database():
    
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    from src.db import session
    
    # create 10 initial boxes
    for x in range(0,10):
        new_address1 = Address(name = 'Buffer Location 221'+str(x),
                               str_name = 'testroad 1',
                               str_no = '112',
                               city = 'Testhausen',
                               post_code = '77682',
                               country = 'Germany',
                               )
        
        session.add(new_address1)
        new_address2 = Address(name='Paul Gluecklich' + str(x),
                               str_name = 'target road',
                               str_no = '22a',
                               city = 'Happyplace',
                               post_code = '12077',
                               country = 'Germany',
                               )
        session.add(new_address2)
        new_box = Box(id=10100+x,
                      name='new box' + str(x), 
                      addr_c=new_address1, 
                      addr_d=new_address2,
                      status = 'ready to ship',
                      weight = '2kg',
                      size = 'M'
                      )
        session.add(new_box) 
        session.commit()

        
if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])

    init_database()
    
    
    