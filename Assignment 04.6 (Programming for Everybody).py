### Assignment 4.6 (Week 6) 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.


# Function to make the calculation of payment
def computepay(h, r):
    # If the hours are 40 or less, multiply for the rate and return
    if h <= 40:
        payment = h * r
        return (payment)
    # If there are more than 40 hours, set the limit hours (40) with minimum payment, and the extra hours with extra rate.
    else:
        # The limited hours for normal pay was set at 40
        limit_hours = 40
        # Extra hours is the result of Hours - Limit Hours
        extra_hours = h - limit_hours
        # Rate for extra hours is 1.5 higher than normal rate
        extra_rate = r * 1.5
        # Make the payment calculation and return
        payment = (limit_hours * r) + (extra_hours * extra_rate)
        return (payment)

# Ask for both, Hours and Rate
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

# Make them Float if cant, send a message error and quit.
try:
    hours = float(hrs)
    pay_rate = float(rate)
except:
    print("Error, please enter a numeric input")
    quit()
# Check if any of two variables equals 0 or lower, if yes, values are wrong
if hours <= 0 or pay_rate <= 0:
    print("The entered values are wrong, please repeat")
    quit()
# Lets call the function
p = computepay(hours, pay_rate)
# Final result
print("Pay:", p)
