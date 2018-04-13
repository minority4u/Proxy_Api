# -*- coding: utf-8 -*-

import os
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from flask import url_for
from src.model_manager import BoxManager

######## setup some global objects #########

box_fields = {
             #'box_id' : fields.Integer,
            'current_adress' : fields.Nested({
                    'first_name' : fields.String}),
            'destination_adress' : fields.Nested({
                    'first_name' : fields.String}),
            'status' : fields.String,
            'size' : fields.String,
            'weight' : fields.String
            }


box_manager = BoxManager()
# register all valid submitted arguments
parser = reqparse.RequestParser()
BOX_ARGS = ['box_id','current_adress','destination_adress','status','size','weight']
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
    
    def abort_if_box_doesnt_exist(self, box_id):
        if box_id not in box_manager.boxes:
            abort(404, message="box {} doesn't exist".format(box_id))
            
    def make_public(self, box, box_id):
        box['uri'] = url_for('boxressource',box_id=box_id,_external=True)
        return box  
            
    @marshal_with(box_fields)
    def get(self, box_id):
        self.abort_if_box_doesnt_exist(box_id)
        return self.make_public(box_manager.get_box(box_id), box_id)

    def delete(self, box_id):
        self.abort_if_box_doesnt_exist(box_id)
        box_manager.delete(box_id)
        return '', 204

    @marshal_with(box_fields)
    def put(self, box_id):
        self.abort_if_box_doesnt_exist(box_id)
        args = self.parser.parse_args()
        box = box_manager.get_box(box_id)
        box.update(args)
        #box_manager[box_id] = box
        return self.make_public(box, box_id), 201


# boxList
# shows a list of all BOXES, and lets you POST to add new tasks
class BoxListRessource(Resource):
    
    def make_public(box, box_id):
        box['uri'] = url_for('boxressource',box_id=box_id,_external=True)
        return box 
    
    @marshal_with(box_fields)
    def get(self):
        return [self.make_public(v) for v in box_manager.boxes.values()]

    
    
    
    
    
    
    