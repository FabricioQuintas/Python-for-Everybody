### Assignment 12.2 (Week 4)

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment.
# One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

## Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link.
# Repeat this process 4 times.
# The answer is the last name that you retrieve.
## Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
## Last name in sequence: Anayah

## Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Harnek.html
# Find the link at position 18 (the first name is 1).
# Follow that link.
# Repeat this process 7 times.
# The answer is the last name that you retrieve.
## Hint: The first character of the name of the last page that you will load is: K

# ------------------------------

# First, import all libs requeried, as urllib, ssl, re, and BeatifulSoup
import re
from turtle import position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# I was constantly giving an error of collections non calleable, so i decided to install this library that helps me with that
import collections
collections.Callable = collections.abc.Callable


# Create the vars
positionSearched = 0
repeatTimes = 0
repeat = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for a URL
url = input('Enter the link (TO DEFAULT DO NOT ENTHER NOTHING): ')
url = url.strip()
# If no url, put the default as 'http://py4e-data.dr-chuck.net/known_by_Harnek.html'
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Harnek.html'

# Ask for a position
positionSearched = int(input('Enter the position needed: '))
# If position is less than 1, send error and quit
if positionSearched < 1:
    print ('The position must be greather than 0')
    quit()
    
# Ask for how many times to repeat, set default as 0
repeatTimes = int(input('Set times to repeat: '))

# While the number of repeat is less than the repeat times needed
while repeat < repeatTimes:
    if len(url) != 0:
        # Then read it, ignoring certificate errors, and use BeatifulSoup to read it
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Set the counter at 0, for a new link
        count = 0
        # Lets get all anchor tags for <a
        tags = soup('a')
        # Itinerate through them all
        for tag in tags:
            # Do 1 to the count of tags viewed
            count = count + 1
            # If the number of count is different to the position needed, continue
            if count != positionSearched: continue
            # If not, set the href as new url and start again the loop
            url = (tag.get('href', None))
            break
    # Add 1 count to the repeat, and start again
    repeat = repeat + 1
# Lets separate the Name from the URL with a try statement
try:
    name = re.findall('known_by_([A-Za-z]+)', url)
    print(name)
except:
    print('Cant find any name on the URL:', url)