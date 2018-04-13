#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:06:14 2018

@author: minority
"""
import os
from flask import Flask
from flask_restful import Api
from src.ressources import BoxRessource, BoxListRessource, BaseDescriptionRessource

app = Flask(__name__)
api = Api(app)
# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9088))



##
## Actually setup the Api resource routing here
##
api.add_resource(BaseDescriptionRessource, '/')
api.add_resource(BoxListRessource, '/boxes/')
api.add_resource(BoxRessource, '/boxes/<int:box_id>')


if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])
    app.run(debug=True, host='0.0.0.0', port=port)