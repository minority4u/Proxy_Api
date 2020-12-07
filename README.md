# Flask based content management API
Contains routes, some Mockdata, supports different db backends which are encapusalted via SQLAlchemy as ORM wrapper. Example implementation of different REST-endpoints. Could be deployed either via docker or via cloud foundry.

# Description
Python based API project for CloudFoundry based deployment.
* Python 3.6.x
* Flask==0.12.2
* SQLAlchemy==1.2.6
* Flask-RESTful==0.3.6



# Setup

* install Python 3.6.x
* install virtualenv
* Clone repo
* create a virtual environment within the repo folder
** virtualenv -p python3 venv
* install all dependencies
** pip install -r requirements.txt
* local deployment with
** python proxy_main.py

# Project overview

![Project Overview](https://github.com/minority4u/Proxy_Api/blob/master/diagrams/Proxy_API%20Class%20diagram.png)


* proxy_main.py
Restful API based on Flask

* src folder
Contains the following modules: db, marshall_fields, model_setup, models, ressources, settings, status

* manifest.yml
Applikation definition for deployment to Cloud Foundry

* requirements.txt
For easy dependency installation via pip

* runtime.txt
Defines the Python interpreter

# Deployment to cloud foundry

zip the following files/folders:
* proxy_main
* requirements.txt
* src
* runtime.txt

Deploy zipfile and manifest.yml to cloud foundry

# TODO
* Code refactoring
* Integrate swagger
* Add minor comments
* Add local debugger
* Add test-client for automated tests

