# Description
Very simple python based API project for CloudFoundry based deployment.
Uses Python 3.6.x
Uses Flask and Flask-Restful


# Setup

* Clone repo
* virtualenv -p python3 venv
* pip install -r requirements.txt
* local run with: python proxy_main.py

# Project files

* proxy_main.py
Restful API based on Flask
API and Ressources within one file to keep it simple

* src folder
model, resources and helper files
Currently there is a box_handler which encapuslates the box creating

* manifest.yml
Applikation definition for deployment to Cloud Foundry

* requierements.txt
For easy dependency installation via pip

* runtime.txt
Defines the Python interpreter

# Deployment

zip the following files/folders:
* proxy_main
* requirements.txt
* src
* runtime.txt

Deploy zipfile and manifest.yml to cloud foundry

# TODO
* Code refactoring
* Encapsulate model and resource definition
* Integrate swagger
* Add minor comments
* Add local debugger
* Add test-client for automated tests
* add database instead of simple json objects
