#import math

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("What operation would you like to perform? \n1. Add (+)\n2. Subtract(-)\n3. Multiply(*)\n4. Divide(/)")
#print("")


operation = input("Enter the option: ")

if operation == "+":
	print (num1+num2)
elif operation == "-":
	print (num1-num2)
elif operation == "*":
	print (num1*num2)
elif operation == "/":
	print (num1/num2)
else:
	print("Wrong Option")

