#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:06:14 2018

@author: minority
"""
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from Ressources.box_handler import Box_Handler

app = Flask(__name__)
api = Api(app)
# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9088))

Data_Handler = Box_Handler()

BOXES = Data_Handler.get_boxes()
ARGS = Data_Handler.get_args()


def abort_if_box_doesnt_exist(box_id):
    if box_id not in BOXES:
        abort(404, message="box {} doesn't exist".format(box_id))

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('title')
parser.add_argument('sender')
parser.add_argument('receiver')
parser.add_argument('status')


# box
# shows a single box item and lets you delete a box item
class Box(Resource):
    def get(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        return BOXES[box_id]

    def delete(self, box_id):
        abort_if_box_doesnt_exist(box_id)
        del BOXES[box_id]
        return '', 204

    def put(self, box_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        BOXES[box_id] = task
        return task, 201


# boxList
# shows a list of all BOXES, and lets you POST to add new tasks
class BoxList(Resource):
    def get(self):
        return BOXES

    def post(self):
        args = parser.parse_args()
        box_id = int(max(BOXES.keys()).lstrip('box')) + 1
        box_id = 'box%i' % box_id
        BOXES[box_id] = {'task': args['task']}
        return BOXES[box_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(BoxList, '/boxes')
api.add_resource(Box, '/box/<box_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)