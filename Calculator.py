num1 = input ("Enter the first number: ")
num2 = input ("Enter the second number: ")

sum = float(num1) + float(num2)	

# Using float() turns the input into a floating point number. 
# You could also use int(), but the program fails if the user enters a floating point number.
# Without these, Python will treat them as strings and concatenate them.


print(sum)

