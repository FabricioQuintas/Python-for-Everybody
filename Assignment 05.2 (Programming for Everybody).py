### Assignment 5.2 (Week 7)
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

# First set the 2 var, largest and smallest with a flag
largest = None
smallest = None
# Make a while iteration to ask for numbers
while True:
    num = input('Enter a number: ')
    # At this time i should make some more changes to the input, like delete spaces and make it all in lowercase
    
    # When the user put "done" the program will stop
    if num == 'done':
        break
    # A try to check if the input is a number
    try:
        # For the exercise u must set the value "float" to "int" to have the same output as needed
        value = float(num)
    # If not a number, send message error and "continue" that will start again the iteration
    except:
        print('Invalid input')
        continue
    # Check both at same time, the flag or if value is higher than the one that we have
    if largest is None or largest < value:
        largest = value
    # Same with the smallest
    if smallest is None or smallest > value:
        smallest = value

# Print needed for exercise
print('Maximum is', largest)
print('Minimum is', smallest)
