# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 

# --------------------------

# Input for Hours and Rate
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
# Try to make them float
try:
    h = float(hrs)
    rt = float(rate)
# If cant, print the error and quit
except:
    print("Error, please enter a numeric input")
    quit()

# If the try works, check quantity of hours
if h > 0:
	if h < 40:
        # If less than 40, hours * rate will be good
		pay = h * rt
	else:
        # Going up to 40, the first 40 must be multiplied by the rate, and the rest (Hours - 40) will be multiplied by (rate * 1.5)
		pay = (40 * rt) + ((h - 40) * (rt * 1.5))
# Print if pay is higher than 0
if pay > 0:
    print("Pay equals to:", pay)
# Final print
else: print("Non assigned pay")