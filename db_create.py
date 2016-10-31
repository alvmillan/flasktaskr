# project/db_create.py


from project import db
#from project.models import Task, User
#from datetime import date


#create the dv and the db table

db.create_all()

#insert data
#db.session.add(User("admin","ad@min.com","admin","admin"))

#db.session.add(Task("Finish this tutotial", date(2015, 3, 13), 10,date(2015,2,13),1, 1))
#db.session.add(Task("Finis Real Python", date(2015, 3, 13), 10,date(2015,2,13),1, 1))

#commit changes

db.session.commit()
"""
with sqlite3.connect(DATABASE_PATH) as connection:

	# Get a cursor
	c = connection.cursor()

	# Create a table

	c.execute(""CREATE TABLE tasks(
		task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		due_date TEXT NOT NULL,
		priority INTEGER NOT NULL,
		status INTEGER NOT NULL)""

	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status)'
		'VALUES("Finish Real Python Course 2", "03/25/2015",10,1)'
		)
		"""