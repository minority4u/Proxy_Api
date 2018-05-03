from sqlalchemy import create_engine
from src.settings import DB_URI
from src.models import Base,Address,Box
from src.db import session


def init_database():

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    # create 10 initial boxes
    for x in range(0 ,10):
        new_address1 = Address(name = 'Buffer Location 221 ' +str(x),
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
        new_box = Box(id=10100 +x,
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