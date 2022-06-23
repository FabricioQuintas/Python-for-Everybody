## Assignment 13.2 (Week 6)

# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
### http://py4e-data.dr-chuck.net/json?

# This API uses the same parameter (address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get "No address..." response.

# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint is as shown above.
# You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.
# ----------------
# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

### $ python3 solution.py
### Enter location: South Federal University
### Retrieving http://...
### Retrieved 2445 characters
### Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8
# ----------------
# Turn In

# Please run your program to find the place_id for this location:
### University of Salamanca

# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below.
# Hint: The first seven characters of the place_id are "ChIJwTu ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API.
# Your program should work with the Google API - but the place_id may not match for this assignment.
# ----------------

# Lets import the library required
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Specify the api_key
api_key = False

# If api_key false, set it as 42 and use the specific API
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    # Ask for a location
    address = input('Enter location: ')
    # If no data given, break
    if len(address) < 1: break

    # Create the dict
    parms = dict()
    # Set the adress key, with the location as value
    parms['address'] = address
    
    # If there is an api_key, create another key with 'key' as name, and the key as value
    if api_key is not False: parms['key'] = api_key
    # Lets encode the url again
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Lets load the data in a TRY, if not, set is as None
    try:
        js = json.loads(data)
    except:
        js = None

    # If STATUS is not "OK", lets print fail and the data
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    # Then, lets print, in results, the place_id
    print('Place id', js['results'][0]['place_id'])