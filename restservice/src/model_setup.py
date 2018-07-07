from sqlalchemy import create_engine
from src.settings import DB_URI
from src.models import Base,Address,Box, Content
from src.db import session


def _create_box_content():
    pass


def init_database():

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    # create 10 initial boxes
    for x in range(0 ,10):

        # create some shoes as demo content
        box_content_1 = Content(name = 'Nike Air Zoom Pegasus 35',
                                style = 'Sneaker',
                                color = 'white',
                                size = 'US 9',
                                price = '85.00 $',
                                condition = 'new'
                                )
        box_content_2 = Content(name='Nike Air Max 270',
                                style='Sneaker',
                                color='black',
                                size='US 9',
                                price= '85.00 $',
                                condition='new'
                                )
        box_contents = [box_content_1, box_content_2]

        # create 10 current addresses with a rising value at the end
        new_current_address = Address(name='Buffer Location 221' + str(x),
                                      str_name='Haven Avenue',
                                      str_no='3645',
                                      city='Menlo Park',
                                      post_code='94025',
                                      state='California',
                                      country='United States of America',
                                      )

        session.add(new_current_address)

        # create 10 destination addresses with a rising value at the end
        new_destination_address = Address(name='Paul Happy',
                                          str_name='Target road',
                                          str_no='42' + str(x),
                                          city='Happyplace',
                                          post_code='94025',
                                          state='California',
                                          country='Germany',
                                          )
        session.add(new_destination_address)

        # create 10 boxes with a current address, a destination address and a content
        new_box = Box(id=10100 + x ,
                      name='new box ' + str(x),
                      addr_c=new_current_address,
                      addr_d=new_destination_address,
                      box_contents = box_contents,
                      status = 'Delivery in Progress',
                      customerStatus = 'Delivered',
                      weight = '2kg',
                      size = 'M'
                      )
        session.add(new_box)
        session.commit()



if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])

    init_database()