### Assignment 8.4 (Week 4)
# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.Y
## You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Ok, at this time i download the .txt archive and store it on the program folder

# Create the list
finalList = list()
# Ask for file name
fname = input("Enter file name: ")
# First lets check if its a correct filename
try:
    file = open(fname)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()
# Itinerate through the text line by line
for line in file:
    # Make a list for each line on the given text
    lineList = line.split()
    # Itinerate for each word on the made list
    for word in lineList:
        # Lets check if the word is not in the list
        if word not in finalList:
            finalList.append(word)
    # Sort the list
    finalList.sort()
# Print the final list that we made
print(finalList)
