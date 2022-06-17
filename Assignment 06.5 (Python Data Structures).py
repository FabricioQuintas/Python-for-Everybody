### Assignment 6.5 (Week 1)
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

# Text given by the course
text = "X-DSPAM-Confidence:    0.8475"

# Lets find the first number, knowing that him comes before the colon
number_position = text.find(':')
# Now that we have the data before the colon, lets delete possible spaces
final_number = text[number_position+1:].strip()
# Make it float and print it
print(float(final_number))
