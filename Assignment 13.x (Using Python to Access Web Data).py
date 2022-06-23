### Assigment 13.x (Week 5)

# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

## Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
## Actual data: http://py4e-data.dr-chuck.net/comments_1565398.xml (Sum ends with 60)

# You do not need to save these files to your folder since your program will read the data directly from the URL.

# First, import all libs requeried, as urllib, ssl and ElementTree
import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create variables
count = 0
total = 0

# Ask for a link
address = input('Enter the link (TO DEFAULT DO NOT ENTHER NOTHING): ')
address = address.strip()
# If no url, put the default as 'http://py4e-data.dr-chuck.net/comments_1565398.xml'
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_1565398.xml'
# Then read it, ignoring certificate errors
data = urllib.request.urlopen(address, context=ctx).read()
# Print the retrieved lenght of data
print ('Retrieved', len(data), 'characters')
# With this we can make the tree for the XML by the library "ET"
tree = ET.fromstring(data)
# This will create a list of all comment in another comment segment
listData = tree.findall('comments/comment')
# Itinerate through each item on the list
for items in listData:
    # Sum +1 to the count of items
    count = count + 1
    # Find the count section and find the number in there with the ".text"
    tot = items.find('count').text
    # Add the count found before to the total number
    total = total + int(tot)

# Print the count, and the final total
print ('Count:', count)
print ('Sum:', total)