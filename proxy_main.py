#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:06:14 2018

@author: minority
"""
import os
from flask import Flask, url_for
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from src.box_handler import Box_Handler
from src.models import BoxModel, AdressModel

app = Flask(__name__)
api = Api(app)
# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9088))

# create some data to play around with
Data_Handler = Box_Handler()
BOXES = Data_Handler.get_boxes()
BOX_ARGS = Data_Handler.get_args()

# register all valid submitted arguments
parser = reqparse.RequestParser()
for box_arg in BOX_ARGS:
    print('register argument ' + box_arg)
    parser.add_argument(box_arg, required=True)



def abort_if_box_doesnt_exist(box_id):
    if box_id not in BOXES:
        abort(404, message="box {} doesn't exist".format(box_id))
        
def make_public(box, box_id):
    box['uri'] = url_for('box',box_id=box_id,_external=True)
    return box      
        

# box
# shows a single box item and lets you delete a box item
class BaseDescription(Resource):
    def get(self):
        
        return {
                'API': 'Proxy API!', 
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)), 
                 'possible routes' : '/boxes/, /boxes/<box-id>'
                 }
        





box_fields = {
             
            'current_FirstName' : fields.String,
            'current_LastName': fields.String,
            'current_Street' : fields.String,
            'current_StreetNo': fields.Integer,
            'current_Plz': fields.Integer,
            'current_City' : fields.String,
            'current_Country' : fields.String,
            'current_StartDate' : fields.DateTime,
            'current_EndDate' : fields.DateTime,
            'destination_FirstName' : fields.String,
            'destination_LastName': fields.String,
            'destination_Street' : fields.String,
            'destination_StreetNo': fields.Integer,
            'destination_Plz': fields.Integer,
            'destination_City' : fields.String,
            'destination_Country' : fields.String,
            'destination_StartDate' : fields.DateTime,
            'destination_EndDate' : fields.DateTime,
            'status' : fields.String,
            'size' : fields.String,
            'weight' : fields.String
            }

class BoxManager():
    last_id = 0
    def __init__(self):
        self.boxes = {}

    def insert_message(self, box):
        self.__class__  .last_id += 1
        box.id = self.__class__.last_id
        self.boxes[self.__class__.last_id] = box

    def get_message(self, id):
        return self.boxes[id]

    def delete_message(self, id):
        del self.boxes[id]

box_manager = BoxManager()



# box
# shows a single box item and lets you delete a box item
class Box(Resource):
    @marshal_with(box_fields)
    def get(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        return make_public(BOXES[box_id], box_id)

    def delete(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        del BOXES[box_id]
        return '', 204

    @marshal_with(box_fields)
    def put(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        args = parser.parse_args()
        box = BOXES[box_id]
        box.update(args)
        BOXES[box_id] = box
        return make_public(box, box_id), 201


# boxList
# shows a list of all BOXES, and lets you POST to add new tasks
class BoxList(Resource):
    @marshal_with(box_fields)
    def get(self):
        return dict((k,make_public(v, k)) for k,v in BOXES.items())

    @marshal_with(box_fields)
    def post(self):
        args = parser.parse_args()
        box_id = int(max(BOXES.keys())) + 1
        box_id = box_id
        BOXES[box_id] = args
        return make_public(BOXES[box_id], box_id), 201

##
## Actually setup the Api resource routing here
##
api.add_resource(BaseDescription, '/')
api.add_resource(BoxList, '/boxes/')
api.add_resource(Box, '/boxes/<int:box_id>')


if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])
    app.run(debug=True, host='0.0.0.0', port=port)