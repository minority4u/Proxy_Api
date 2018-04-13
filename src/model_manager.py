# -*- coding: utf-8 -*-
from src.models import BoxModel
import json


class BoxManager():
    last_id = 0
    def __init__(self):
        self.boxes = {}
        
        # init some boxes
        curr = {'first_name' : 'bernd'}
        dest = {'first_name' : 'bernd_dest'}
        box = BoxModel(curr, dest, 'ready', 'M', '2kg')
        self.insert_box(box)
        

    def insert_box(self, box):
        self.__class__  .last_id += 1
        box.id = self.__class__.last_id
        self.boxes[self.__class__.last_id] = box

    def get_box(self, id):
        return self.boxes[id]

    def delete_box(self, id):
        del self.boxes[id]

if __name__ == '__main__':
    import os
    
    print(os.path.splitext("path_to_file")[0])
    box_manager = BoxManager()
    
    curr = {'first_name' : 'bernd'}
    dest = {'first_name' : 'bernd_dest'}
    box = BoxModel(curr, dest, 'ready', 'M', '2kg')
    box_manager.insert_box(box)
    print(json.dumps(box_manager.boxes))
    
    
    
