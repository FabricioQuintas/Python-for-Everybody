## Assignment 13.1 (Week 6)

# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

## Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
## Actual data: http://py4e-data.dr-chuck.net/comments_1565399.json (Sum ends with 97)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.


# First lets import the json library and urllib request
import json
import urllib.request

# Start the count at 0
count = 0

# Request for a URL, if nothing, put as default "http://py4e-data.dr-chuck.net/comments_1565399.json"
url = input('Please enter a URL (TO DEFAULT DO NOT ENTHER NOTHING):')
url = url.strip()

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1565399.json'
print('Retrieving', url)
# Open the URL with urlopen and read it with json as try
try: 
    # Use urllib library to access it
    data = urllib.request.urlopen(url)
    # Load it as json
    info = json.loads(data.read())
# If cant do the open/load, print a message error and quit
except:
    print("The URL cannot be opened as json file")
    quit()

# Itinerate through each item in sector "comments"
for item in info["comments"]:
    # Then add the count of that dict to our count
    count = count + int(item['count'])
# Finally, print it
print('Total Sum:', count)