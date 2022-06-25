## Assignment 15.2 (Week 2)

### Counting Organizations

# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

### CREATE TABLE Counts (org TEXT, count INTEGER)

# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data.
# The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop.
# In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
# ---------------------------

# First lets import SQLite3
import sqlite3

# Lets make a connection with 'emaildb.sqlite' if not there, it will create one
connection = sqlite3.connect('Assignment15.sqlite')
# And make a cursor to work in
work = connection.cursor()

# Then lets delete all data in, if there is any data
work.execute('DROP TABLE IF EXISTS Counts')
# And create a new table
work.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Request for a file name, if nothing, put as default "mbox.txt"
name = input('Enter a file name (TO DEFAULT DO NOT ENTHER NOTHING) :')
if len(name) < 1:
    name = 'mbox.txt'

# First lets check if its a correct filename
try:
    file = open(name)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()

for line in file:
    # Lets rstrip the line to delete possible '\n' and split it in a new list
    line = line.rstrip()
    words = line.split()
    # Guardian in a compound statement
    if len(words) < 2 or words[0] != 'From:':
        continue
    # Separate the mail word for his "@" and select the 2nd part of it, it will be the organization
    organization = words[1].split('@')[1]
    # Select the row where ORG equals our organization stored in the var
    work.execute('SELECT count FROM Counts WHERE org = ? ', (organization,))
    # And store it in a variable called "row"
    row = work.fetchone()

    # Then, check if the row have some value, if not, add the organization with value 1, if it already is sum 1 to the count
    if row is None:
        # If there is no value, add the row with organization as "org", and 1 on the value of it
        work.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organization,))
    else:
        # Else, UPDATE it, counting 1 more to the count section
        work.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(organization,))
    # And send the packages
    connection.commit()
# Finally, make a STATEMENT to grab the top count from the SQL
topCount = work.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
# And print it
print(topCount.fetchone())
