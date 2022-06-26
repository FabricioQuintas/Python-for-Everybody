## Assignment 15.3 (Week 3)

### Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

'''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
); 
'''

# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

# You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

'''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
'''

# -----------------------------

# Lets import ElementTree and SQLite
import xml.etree.ElementTree as ET
import sqlite3

# Lets make a connection with 'emaildb.sqlite' if not there, it will create one
connection = sqlite3.connect('Assignment15-3.sqlite')
# And make a cursor to work in
work = connection.cursor()

# Make some fresh tables using executescript()
# Deleting all tables if exits, such as Artist, Genre, Album, Track
# And creating them from 0
   ## Artist has ID Unique with Autoincrement, and a NAME Text Unique
   ## Genre has ID Unique with Autoincrement, and a NAME Text Unique
   ## Album has ID Unique with Autoincrement, an Artist_ID (From Artist) and a TITLE Text Unique
   ## Track has ID Unique with Autoincrement, TITLE Text Unique, Genre_ID (From Genre), Album_ID (From Album) and LEN - RATING - COUNT as Integers
work.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    genre_id INTEGER,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Ask for a fileName
fileName = input('Enter file name (TO DEFAULT DO NOT ENTHER NOTHING) : ')
# If len less than 1, set it as "Library.xml"
if ( len(fileName) < 1 ) :
    fileName = "library.xml"

# Make an fuction to look for the row/key
def lookup(d, key):
    # Set a variable FOUND as False
    found = False
    # Itinerate through each line of the "Track" given as parameter
    for child in d:
        # This come after the next line, so this will return the text after the key found
        if found:
            return child.text
        # Lets check if the tag of the line is the key needed, if it is, set found as True
        if child.tag == 'key' and child.text == key:
            found = True
    return None

try:
    # Lets parse it with ET
    stuff = ET.parse(fileName)
except:
    # If cant, print a message error and quit
    print('That file cant be procesed')
    quit()

# Find all Dict on Dict on Dict, that's the format of XML from iTunes
all = stuff.findall('dict/dict/dict')
# And print the len of all tracks found
print('Dict count:', len(all))

# Lets itinerate through 'all'
for entry in all:
    # If no 'Track ID', continue
    if ( lookup(entry, 'Track ID') is None ) : continue
    # Lookup for all names with the function made, sending all the "Track" and itinerate through it looking for the Key word
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    # If name/artist/album/genre is None, continue
    if name is None or artist is None or album is None or genre is None: continue
    # print(name, artist, album, genre, count, rating, length)

    # INSERT or IGNORE the name of each Artist
    work.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
    # And grab his ID to use on the ALBUM statement
    work.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = work.fetchone()[0]

    # INSERT or IGNORE genre name
    work.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) )
    # And grab his ID to use on TRACK statement
    work.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = work.fetchone()[0]

    # INSERT or IGNORE artist_id and title INTO Album
    work.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    # And grab his ID to use on the next statement
    work.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = work.fetchone()[0]

    # INSERT or REPLACE all values into TRACK
    work.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ? )''', ( name, album_id, genre_id, length, rating, count ))
    
    # Close connection
    connection.commit()
