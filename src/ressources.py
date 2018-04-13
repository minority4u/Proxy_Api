# -*- coding: utf-8 -*-
from src.models import Box
from src.db import session

import os
from flask_restful import reqparse, abort, Resource, fields, marshal_with


######## setup some global objects #########

box_fields = {
             'id':fields.Integer,
             'name' : fields.String,
             'uri' : fields.Url('boxressource', absolute=True)
            }



# register all valid submitted arguments
parser = reqparse.RequestParser()
BOX_ARGS = ['name']
for box_arg in BOX_ARGS:
    print('register argument ' + box_arg)
    parser.add_argument(box_arg, required=True)



# box
# shows a single box item and lets you delete a box item
class BaseDescriptionRessource(Resource):            
    def get(self):
        
        return {
                'API': 'Proxy API!', 
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)), 
                 'possible routes' : '/boxes/, /boxes/<box-id>'
                 }
        

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
        parsed_args = parser.parse_args()
        box = session.query(Box).filter(Box.id == id).first()
        box.name = parsed_args['name']
        session.add(box)
        session.commit()
        return box, 201


# boxList
# shows a list of all BOXES, and lets you POST to add a new box
class BoxListRessource(Resource):
    
    @marshal_with(box_fields)
    def get(self):
        boxes = session.query(Box).all()
        return boxes
    
    @marshal_with(box_fields)
    def post(self):
        parsed_args = parser.parse_args()
        box = Box(name=parsed_args['name'])
        session.add(box)
        session.commit()
        return box, 201

    
    
    
    
    
    
    