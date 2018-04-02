# Description
Simple python based API project for CloudFoundry based deployment.
Uses Python 3.6.x


# Setup

* Clone repo

* virtualenv -p python3 venv

* pip install -r requirements.txt

* local run
'''python
python main.py

'''


# Project files

* proxy_main.py
Restful API based on Flask

* Ressources folder
model and helper definitions

* manifest.yml
Applikation definition for deployment to Cloud Foundry

* runtime.txt
Defines the Python interpreter

# Deployment

zip the following files/folders:
* proxy_main
* requirements.txt
* Ressources
* runtime.txt

Deploy zipfile and manifest.yml to cloud foundry
