# Assignment 8.5 (Week 4)
# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

## Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.
## You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Create the variable
count = 0
# Ask for file name
fname = input("Enter file name: ")
# First lets check if its a correct filename
try:
    file = open(fname)
except:
    # If not, send message error and quit program
    print('Please enter a correct file name')
    quit()
# Itinerate through each line in text
for line in file:
    # Make it lowercase and eliminate extra spaces (\n) from the right
    line = line.lower()
    line = line.rstrip()
    # Check if the line start with 'from'
    if line.startswith('from '):
        # And omit if start with 'from:'
        if not line.startswith('from:'):
            # Split it in a new list, sum to the count
            splittedLine = line.split()
            count = count + 1
            # Print the position 1 of the list (knowing that the line is ""From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"")
            print(splittedLine[1])
# Then, do the final print with the count of lines that contain a "From " at first
print("There were", count, "lines in the file with From as the first word")

# --------------------------------------------------------

#### Another way easier to make it

# Create the variable
count = 0
# Ask for file name
fname = input("Enter file name: ")
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
    wds = line.split()
    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    if wds[0] == 'From':
        # Print the position 1 of the list (knowing that the line is ""From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"")
        print(wds[1])
        # Count it
        count = count + 1
# Then, do the final print with the count of lines that contain a "From " at first
print("There were", count, "lines in the file with From as the first word")
