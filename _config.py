import os

# grab the folder where this script live

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE ='flasktaskr.db'
#USERNAME ='admin'
#PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY ='myprecious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)


# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
