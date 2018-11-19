# TaskList
Django task list

**Author**: Kristian Koci

## Requirements
* Python 3.6
* Django 1.9 
* django-bootstrap
* django-bootstrap-form
* django-datetime-widget
* SQLite 3+ 

## First create a virtualenv environment with virtualenvwrapper
mkvirtualenv my_proj

If You wanna use a particular python version installed on your system then:
mkvirtualenv -p /usr/bin/python3.x my_proj

After that:
workon my_proj

pip install -r requirements.txt

## DB generation
You should use the migrate Django command

Run command
> python manage.py migrate

## How to launch the app?
Run command
> python manage.py runserver

By default you can use the app at http://localhost:8000

## Tests
There are 4 tests, 3 http simple ones, and one database TestCase

On the root app folder just run
> python manage.py test TaskList