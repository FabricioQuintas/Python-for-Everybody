## Assignment 15.4 (Week 4)

## Instructions
# This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

# Each student gets their own file for the assignment.
# Download this file and save it as roster_data.json.
# Move the downloaded file into the same folder as your roster.py program.

# Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:
'''
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''

# The output should look as follows:
'''
Zunairah|si364|0
Zishan|si301|0
'''

# Once that query gives the correct data, run this query:
'''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
'''
# You should get one row with a string that looks like XYZZY53656C696E613333.

# ---------------------------

# Lets import sqlite3 and json
import sqlite3
import json

# Lets make a connection with 'emaildb.sqlite' if not there, it will create one
connection = sqlite3.connect('Assignment15-4.sqlite')
# Make a cursor to work in
work = connection.cursor()

# Make some fresh tables using executescript()
# Deleting all tables if exits, such as User, Member and Course
# And creating them from 0
   ## User has ID Unique with Autoincrement, and a NAME Text Unique
   ## Course has ID Unique with Autoincrement, and a TITLE Text Unique
   ## Member has two primary keys, USER_ID (from User) and COURSE_ID (from Course), and a role setted 0 for Student, and 1 for Teacher
connection.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Ask for a fileName
fileName = input('Enter file name (TO DEFAULT DO NOT ENTHER NOTHING) : ')
# If len less than 1, set it as "roster_data.json"
if ( len(fileName) < 1 ) :
    fileName = "roster_data.json"

# This is an example of this data:
  ##   [ "Chizaram", "si110", 1 ], [ ... ], [ ... ], ...

# Lets make an try to open and load, if cant print an error and quit
try:
    # Open archive and read
    xData = open(fileName).read()
    # Load as json archive
    data = json.loads(xData)
except:
    print('This file cant be loaded')
    quit()

# Lets itinerate through all the data
for person in data:
    # if there is less than 3 objects in the person, continue
    if len(person) < 3: continue
    # The name is the first string, course the second, and at last the role (in integer)
    name = person[0]
    course = person[1]
    role = int(person[2])
    # Lets print them all
    print (name, course, role)

    # Lets insert or ignore the name into User
    work.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', ( name, ) ) # The ? statement is a position for, in this case, name
    work.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = work.fetchone()[0]

    work.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( course, ) ) # The ? statement is a position for, in this case, title
    work.execute('SELECT id FROM Course WHERE title = ? ', (course, ))
    course_id = work.fetchone()[0]

    work.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', ( user_id, course_id, role) ) # In this case, there is "? ? ?", and are position for all 3 vars

    # Close the connection
    connection.commit()