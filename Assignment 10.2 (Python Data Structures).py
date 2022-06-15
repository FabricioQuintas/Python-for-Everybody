### Assignment 10.2 (Week 6)
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#### From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

hoursCount = dict()

# Ask for file name
fname = input("Enter file:")
# First lets check if its a correct filename
try:
    file = open(fname)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()

for line in file:
    # Eliminate extra spaces (\n) from the right and split it in a new list
    line = line.rstrip()
    words = line.split()
    # Guardian in a compound statement
    if len(words) < 5 or words[0] != 'From':
        continue
    # Lets check if its exactly the statement 'From'
    if words[0] == 'From':
        # Extract the spot 5 of the line (hour,minutes,second) that are splitted by a colon
        fullHours = words[5].split(':')
        # Put it in a new var
        Hour = fullHours[0]
        # Add it to the dictionary if not there, or sum +1 if its there
        hoursCount[Hour] = hoursCount.get(Hour, 0) + 1
# Finally, itinerate through the sorted dictionary by key and print it
for key,value in sorted(hoursCount.items()):
    print (key, value)
