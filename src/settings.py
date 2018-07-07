# -*- coding: utf-8 -*-

# define the underlying database
#DB_URI = 'sqlite:///./main.db'
#DB_URI = 'postgresql://usr:test@postgresdb/sqlalchemy'
DB_URI = 'mysql+pymysql://usr:test@mysqldb/sqlalchemy'

# define
##API_PORT = 9088

# define Flask behaviour
APP_CONFIG = {
    # return all errors for wrong requests at once
    'BUNDLE_ERRORS' : True,
    'SERVER_PORT' : 5000
}


# Define all valid request params and map them to a context
valid_request_arguments = {
    'User' : ['api'],
    'Address' : ['name', 'str_name', 'str_no', 'city', 'post_code', 'country','start_date', 'end_date'],
    'Box' : ['name', 'status', 'customerStatus', 'weight', 'size'],
    'Content' : ['name', 'style', 'size', 'price', 'condition']
}
