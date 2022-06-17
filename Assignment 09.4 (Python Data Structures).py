### Assignment 9.4 (Week 5)
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Create Variables
mailsDict = dict()
highestValue = None
highestKey = None

# Ask for file name
name = input("Enter file:")
# First lets check if its a correct filename
try:
    file = open(name)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()
# Lets itinerate through each line of the text
for line in file:
    # Lets rstrip the line to delete possible '\n' and split it in a new list
    line = line.rstrip()
    words = line.split()
    # Guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    # If words is exactly the same as needed
    if words[0] == 'From':
        # Store the mail in a new var
        word = words[1]
        # Add it to the dict if its not there, if is there sum +1
        mailsDict[word] = mailsDict.get(word, 0) + 1
# Finally, lets search for the highest key and value
for key, value in mailsDict.items():
    # If the value is None, or higher than the stored, store key and value
    if highestValue is None or value > highestValue:
        highestKey = key
        highestValue = value
# Print the highest Key and highest Value
print(highestKey, highestValue)

