### Assignment 7.1 (Week 3) 
# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
## You can download the sample data at http://www.py4e.com/code3/words.txt

# Ok, at this time i already made an "words.txt" and put it on this program folder

# Use words.txt as the file name
fileName = input("Enter file name: ")
# Lets check if the file name can be read
try:
    finalFile = open(fileName.strip())
# If cant be read, print a message error and quit
except:
    print('Please enter a valid file name')
    quit()
# Then, if its a correct file name
# Search throught the data
for lines in finalFile:
    # Lets make it upper
    uppercaseLine = lines.upper()
    # Delete extra spaces on the right to avoid innecesary extra lines and print
    print(uppercaseLine.strip())