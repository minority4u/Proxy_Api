# -*- coding: utf-8 -*-
from src.models import Box, Address
from src.db import session

import os
from flask_restful import reqparse, abort, Resource, fields, marshal_with


######## setup some global objects #########

address_fields_c = {
        'id': fields.Integer,
     'name':fields.String,
     'str_name':fields.String,
     'str_no':fields.String,
     'city' : fields.String,
     'post_code':fields.String,
    'country' : fields.String,
    'start_date': fields.DateTime,
    'end_date': fields.DateTime,
}

address_fields_d = {
        'id': fields.Integer,
     'name':fields.String,
     'str_name':fields.String,
     'str_no':fields.String,
     'city' : fields.String,
     'post_code':fields.String,
    'country' : fields.String,
    'start_date': fields.DateTime,
    'end_date': fields.DateTime,
}


box_fields = {
             'id':fields.Integer,
             'uri' : fields.Url('boxressource', absolute=True),
             'name' : fields.String,
            'status': fields.String,
            'weight': fields.String,
            'size': fields.String,

             'addr_c' :fields.Nested(address_fields_c),
             'addr_d': fields.Nested(address_fields_d),

             
            }

box_fields_reduced = {
             'id':fields.Integer,
             'uri' : fields.Url('boxressource', absolute=True),
             'name' : fields.String,
             'status' : fields.String,
             'weight' : fields.String,
             'size' : fields.String,
            }

# register valid params
parser = reqparse.RequestParser()

# register all valid Address  arguments
ADDRESS_ARGS = ['name', 'str_name', 'str_no', 'city', 'post_code', 'country','start_date', 'end_date']
for addr_arg in ADDRESS_ARGS:
    print('register Address argument ' + addr_arg)
    parser.add_argument(addr_arg, location = ['headers','form','args'])

# register all valid Box  arguments
BOX_ARGS = ['name', 'status', 'weight', 'size']
for box_arg in BOX_ARGS:
    print('register Box argument ' + box_arg)
    parser.add_argument(box_arg, location = ['headers','form','args'])



# root
# shows the possible routes
class BaseDescriptionRessource(Resource):            
    def get(self):
   
        return {
                'App': 'Proxy API!',
                'vers.:' : 'vers.: 0.2',
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)), 
                 'possible routes' : '/boxes/, /boxes/<int:box-id>'
                 }


# box
# shows a single box item and lets you delete a box item
class AddressRessource(Resource):

    @marshal_with(address_fields_d)
    def get(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Address {} doesn't exist".format(id))
        return address

    def delete(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Box {} doesn't exist".format(id))
        session.delete(address)
        session.commit()
        return {}, 204

    @marshal_with(address_fields_d)
    def put(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Address {} doesn't exist".format(id))

        parsed_args = parser.parse_args()
        for addr_arg in ADDRESS_ARGS:
            if addr_arg in parsed_args and parsed_args[addr_arg]:
                setattr(address, addr_arg, parsed_args[addr_arg])

        session.commit()
        return address, 201

# box
# shows a single box item and lets you delete a box item
class BoxRessource(Resource):
            
    @marshal_with(box_fields)
    def get(self, id):
        box = session.query(Box).filter(Box.id == id).first()
        if not box:
            abort(404, message="Box {} doesn't exist".format(id))
        return box

    def delete(self, id):
        box = session.query(Box).filter(Box.id == id).first()
        if not box:
            abort(404, message="Box {} doesn't exist".format(id))
        session.delete(box)
        session.commit()
        return {}, 204

    @marshal_with(box_fields)
    def put(self, id):
        box = session.query(Box).filter(Box.id == id).first()
        if not box:
            abort(404, message="Box {} doesn't exist".format(id))

        parsed_args = parser.parse_args()
        for box_arg in BOX_ARGS:
            if box_arg in parsed_args and parsed_args[box_arg]:
                setattr(box, box_arg, parsed_args[box_arg])

        session.commit()
        return box, 201


# boxList
# shows a list of all BOXES, and lets you POST to add a new box
class BoxListRessource(Resource):
    
    @marshal_with(box_fields_reduced)
    def get(self):
        boxes = session.query(Box).all()
        print(boxes)
        return boxes
    
    @marshal_with(box_fields)
    def post(self):
        parsed_args = parser.parse_args()
        box = Box(**parsed_args)
        session.add(box)
        session.commit()
        return box, 201


# boxList
# shows a list of all BOXES, and lets you POST to add a new box
class AddressListRessource(Resource):

    @marshal_with(address_fields_c)
    def get(self):
        addresses = session.query(Address).all()
        print(addresses)
        return addresses

    @marshal_with(address_fields_c)
    def post(self):
        parsed_args = parser.parse_args()
        address = Address(**parsed_args)
        session.add(address)
        session.commit()
        return address, 201
    
    
    
    
    
    