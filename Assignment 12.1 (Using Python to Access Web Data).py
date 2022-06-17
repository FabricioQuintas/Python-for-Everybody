### Assignment 12.1 (Week 4)

# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

### Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
### Actual data: http://py4e-data.dr-chuck.net/comments_1565396.html (Sum ends with 3)

# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# ----------------------

## Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

#** <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#** <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#** <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

# ----------------------

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# First, import all libs requeried, as urllib, ssl, re, and BeatifulSoup
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# I was constantly giving an error of collections non calleable, so i decided to install this library that helps me with that
import collections
collections.Callable = collections.abc.Callable

# Create the total sum var
totalSum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for a URL
url = input('Enter a url:')
# If no url, put the default as 'http://py4e-data.dr-chuck.net/comments_1565396.html'
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1565396.html'
    
# Try to read it, if not, print an error and quit
try:
    # Then read it, ignoring certificate errors
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print('That URL cant be procesed')
    quit()

# And use BeatifulSoup to read it
soup = BeautifulSoup(html, 'html.parser')


# Get the span tags, easier for the BeatifulSoup library
tags = soup('span')
# Search through all span tags
for tag in tags:
   # Look at the parts of a tag
   y = str(tag)
   # Get the number of the curent tag
   x = re.findall('[0-9]+', y)
   # Knowing that i get only one number per comment i know that the list only have 1 spot and add it to the totalSum
   totalSum = totalSum + int(x[0])
# Print the totalSum
print (totalSum)
