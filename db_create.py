# flasktaskr/db_create.py
'''
import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
        status INTEGER NOT NULL)""")

    # insert dummy data into the table
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
    )

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
    )
'''

from views import db
from models import Task
from datetime import date

# create a database and the db table

db.create_all()

# insert data
db.session.add(Task("Finish this tutorial",date(2017, 02, 7), 10, 1))
db.session.add(Task("Finish Real Python",date(2017, 03, 7), 10, 1))

# commit the changes
db.session.commit()

