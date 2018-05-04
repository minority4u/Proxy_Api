#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:06:14 2018

@author: minority
"""
import os
from flask import Flask
from flask_restful import Api
from src.ressources import BoxRessource, BoxListRessource, BaseDescriptionRessource, AddressListRessource, AddressRessource
#from src.models import init_database
from src.model_setup import init_database
#from src.settings import API_PORT
from src.settings import APP_CONFIG

app = Flask(__name__)
api = Api(app)

# define the overall app configuration
app.config.update(APP_CONFIG)

# Get port from environment variable or choose 9088 as local default
port = int(os.getenv("PORT", APP_CONFIG['SERVER_PORT']))

# drop the old table, setup a new database if no exists, create tables
init_database()

##
## Actually setup the Api resource routing here
##
api.add_resource(BaseDescriptionRessource, '/')
api.add_resource(BoxListRessource, '/boxes/')
api.add_resource(BoxRessource, '/boxes/<int:id>')
api.add_resource(AddressListRessource, '/addresses/')
api.add_resource(AddressRessource, '/addresses/<int:id>')



if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])
    app.run(debug=True, host='0.0.0.0', port=port)