# -*- coding: utf-8 -*-
from sqlalchemy.orm import joinedload

from src.models import Box, Address, Rootdescription, Content
from src.db import session
from src.marshall_fields import *
from src.settings import valid_request_arguments
from flask_restful import reqparse, abort, Resource, marshal_with, marshal

def create_request_parser(request_args):
    # register valid params
    parser = reqparse.RequestParser()
    for key, parameterlist in request_args.items():
        for parameter in parameterlist:
            print('register {0:s} argument: {1:s}'.format(key,parameter))
            parser.add_argument(parameter,location = ['headers', 'form', 'args'])
    return parser


# setup some module objects
parser = create_request_parser(request_args=valid_request_arguments)

# for debugging purpose
def print_args():
    parsed_args = parser.parse_args()
    for arg in parsed_args.items():
        print(arg)


# root
# shows the possible routes
class BaseDescriptionRessource(Resource):

    def get(self):
        parsed_args = parser.parse_args()
        if parsed_args['api'] == 1:
            return marshal(Rootdescription, base_field_full)
        else:
            return marshal(Rootdescription, base_field_reduced)


# address
# shows a single address item and lets you change and delete a address item
class AddressRessource(Resource):

    @marshal_with(address_fields_full)
    def get(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Address {} doesn't exist".format(id))
        return address

    def delete(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Address {} doesn't exist".format(id))
        session.delete(address)
        session.commit()
        return {}, 204

    @marshal_with(address_fields_full)
    def put(self, id):
        address = session.query(Address).filter(Address.id == id).first()
        if not address:
            abort(404, message="Address {} doesn't exist".format(id))
        ADDRESS_ARGS = valid_request_arguments['Address']
        parsed_args = parser.parse_args()
        for addr_arg in ADDRESS_ARGS:
            if addr_arg in parsed_args and parsed_args[addr_arg]:
                setattr(address, addr_arg, parsed_args[addr_arg])

        session.commit()
        return address, 201

# address
# shows a single address item and lets you change and delete a address item
class ContentRessource(Resource):

    @marshal_with(box_content_fields)
    def get(self, id):
        content = session.query(Content).filter(Content.id == id).first()
        if not content:
            abort(404, message="Content {} doesn't exist".format(id))
        return content

    def delete(self, id):
        content = session.query(Address).filter(Address.id == id).first()
        if not content:
            abort(404, message="Content {} doesn't exist".format(id))
        session.delete(content)
        session.commit()
        return {}, 204

    @marshal_with(box_content_fields)
    def put(self, id):
        content = session.query(Content).filter(Content.id == id).first()
        if not content:
            abort(404, message="Address {} doesn't exist".format(id))
        CONTENT_ARGS = valid_request_arguments['Content']
        parsed_args = parser.parse_args()
        for addr_arg in CONTENT_ARGS:
            if addr_arg in parsed_args and parsed_args[addr_arg]:
                setattr(content, addr_arg, parsed_args[addr_arg])

        session.commit()
        return content, 201

# box
# shows a single box item and lets you change and delete a box item
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
        BOX_ARGS = valid_request_arguments['Box']
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


# addressList
# shows a list of all Addresses, and lets you POST to add a new address
class AddressListRessource(Resource):

    @marshal_with(address_fields_full)
    def get(self):
        addresses = session.query(Address).all()
        print(addresses)
        return addresses

    @marshal_with(address_fields_full)
    def post(self):
        parsed_args = parser.parse_args()
        address = Address(**parsed_args)
        session.add(address)
        session.commit()
        return address, 201
    

# addressList
# shows a list of all Addresses, and lets you POST to add a new address
class ContentListRessource(Resource):

    @marshal_with(box_content_fields)
    def get(self):
        contents = session.query(Content).all()
        print(contents)
        return contents

    @marshal_with(box_content_fields)
    def post(self):
        parsed_args = parser.parse_args()
        content = Address(**parsed_args)
        session.add(content)
        session.commit()
        return content, 201
    
    
    
    