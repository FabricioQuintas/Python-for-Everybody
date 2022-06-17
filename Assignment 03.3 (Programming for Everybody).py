### Assignment 03.3 (Week 5) 
# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
## Score Grade
#       >= 0.9 A
#       >= 0.8 B
#       >= 0.7 C
#       >= 0.6 D
#       < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 
### For the test, enter a score of 0.85.

# -------------------------------

# Input the Score and make it float
score = input("Enter Score between 0 and 1: ")
try:
	sc = float(score)
# If cant make it float, sent an error and quit
except: 
	print("Error, please enter a numeric input")
	quit()

# If the score is between 0.0 and 1.0, check score and print it
if sc >= 0 and sc <= 1:
	if sc >= 0.9:
		print("The score is A")
	elif sc >= 0.8:
		print("The score is B")
	elif sc >= 0.7:
		print("The score is C")
	elif sc >= 0.6:
		print("The score is D")
	else:
		print("The score is F")
# If score not between 0 and 1, print message error
else:
    print("Invalid score")

