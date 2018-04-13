# Description
Very simple python based API project for CloudFoundry based deployment.
* Python 3.6.x
* FFlask==0.12.2
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

# Project files

* proxy_main.py
Restful API based on Flask
API and Ressources within one file to keep it simple

* src folder
model, resources and helper files

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

