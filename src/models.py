# -*- coding: utf-8 -*-

from sqlalchemy import Column
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
     str_name = Column(String(250))
     str_no = Column(String(250))
     city = Column(String(250))
     post_code = Column(String(250))




class Box(Base):
    __tablename__ = 'box'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    addr_c_id = Column(Integer, ForeignKey('address.id'))
    addr_c = relationship(Address,foreign_keys=[addr_c_id], lazy='joined')
    
    addr_d_id = Column(Integer, ForeignKey('address.id'))
    addr_d = relationship(Address, foreign_keys=[addr_d_id], lazy = 'joined')




def init():
    
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    from src.db import session
    
    new_address1 = Address(name = 'Buffer Location 2213',
                           str_name = 'testroad 1',
                           str_no = '112',
                           city = 'Testhausen',
                           post_code = '77682')
    
    session.add(new_address1)
    session.commit()
    new_address2 = Address(name='Paul Gluecklich',
                           str_name = 'target road',
                           str_no = '22a',
                           city = 'Happyplace',
                           post_code = '12077')
    session.add(new_address2)
    session.commit()
    new_box = Box(name='new box', addr_c=new_address1, addr_d=new_address2)
    
    session.add(new_box)
    

    
#    new_address = Address(street_name='Teststreet', person = new_person)
#    session.add(new_address)
    
    session.commit()

        
if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])

    init()
    
    
    