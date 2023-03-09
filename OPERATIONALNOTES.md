# Overview
Django web application

# Setup
## Create virtual environment
python -m venv env
. env/Scripts/activate
pip install django==3.1
pip freeze > requirments.txt
## Create project
django-admin.exe startproject ecommerce

## Create apps
python manage.py startapp category
python manage.py startapp account
python manage.py startapp store

## Migrate models
### Create migrations from models
python manage.py makemigrations
### Apply migrations
python manage.py migrate

## create superuser
python manage.py createsuperuser
steventongsf@gmail.com:admin


## Install support for https
pip install django-extensions Werkzeug


# Local deployment and runtime
## Run server
python manage.py runserver

## Deploy static files
python manage.py  collectstatic

## Tools
* DB Browser for SQLite
* SQLite Studio
* VS Code

## VS Code Debugging Setup
* Select Run -> Add Configuration...
  * Select Python
  * Select Django
