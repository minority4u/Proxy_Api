#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:06:14 2018

@author: minority
"""
import os
from flask import Flask, jsonify, url_for
from flask_restful import reqparse, abort, Api, Resource
from Ressources.box_handler import Box_Handler

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
        
def make_public(box):
    public_box = {}
    for field in box:
        if field == 'id':
            public_box['uri'] = url_for('box',box_id=box[field],_external=True)
        else:
            public_box[field] = box[field]
    return public_box      
        

# box
# shows a single box item and lets you delete a box item
class BaseDescription(Resource):
    def get(self):
        
        return {
                'API': 'Proxy API!', 
                'Instance' : str(os.getenv("CF_INSTANCE_INDEX", 0)), 
                 'possible routes' : '/boxes/, /boxes/<box-id>'
                 }


# box
# shows a single box item and lets you delete a box item
class Box(Resource):
    def get(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        return make_public(BOXES[box_id])

    def delete(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        del BOXES[box_id]
        return '', 204

    def put(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        args = parser.parse_args()
        box = BOXES[box_id]
        box.update(args)
        BOXES[box_id] = box
        return make_public(box), 201


# boxList
# shows a list of all BOXES, and lets you POST to add new tasks
class BoxList(Resource):
    def get(self):
        return dict((k,make_public(v)) for k,v in BOXES.items())

    def post(self):
        args = parser.parse_args()
        box_id = int(max(BOXES.keys()).lstrip('box')) + 1
        box_id = 'box%i' % box_id
        BOXES[box_id] = {'task': args['task']}
        return BOXES[box_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(BaseDescription, '/')
api.add_resource(BoxList, '/boxes/')
api.add_resource(Box, '/boxes/<int:box_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)