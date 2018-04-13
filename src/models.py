# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
from sqlalchemy import create_engine
from src.settings import DB_URI
engine = create_engine(DB_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

class Box(Base):
    __tablename__ = 'boxes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))



        
if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])
