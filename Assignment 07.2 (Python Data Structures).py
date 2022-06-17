### Assignment 7.2 (Week 3)
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
## " X-DSPAM-Confidence:    0.8475 ""
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
## You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Ok, at this time i download the .txt archive and store it on the program folder
# Create variables
correctLines = 0
coreValue = 0
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
# First lets check if its a correct filename
try:
    fh = open(fname)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()
# Then lets check for each text line
for line in fh:
    # If the line doesn't have the requested text, continue with other line
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # If it have that part of text, removes it from text
    numberInLine = line.replace("X-DSPAM-Confidence:", '')
    # Count the line to make an average
    correctLines = correctLines + 1
    # Sum the value of the line with value stored
    coreValue = coreValue + float(numberInLine.strip())
# Then, finally divide between the value stored, and the total lines with the correct text and print it
print("Average spam confidence:", float(coreValue/correctLines))
