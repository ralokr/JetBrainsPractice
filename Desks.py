desks = 0

print("Enter number of students in each group: ")

num_class1 = abs(int(input()))
num_class2 = abs(int(input()))
num_class3 = abs(int(input()))

if num_class1 > 1000:
	print('Enter count for class 1 again')
	num_class1 = abs(int(input()))

if num_class2 > 1000:
	print('Enter count for class 2 again')
	num_class2 = abs(int(input()))

if num_class3 > 1000:
	print('Enter count for class 3 again')
	num_class3 = abs(int(input()))

if num_class1 % 2 == 0:
  desks = desks + (num_class1 / 2)
else:
  desks = desks + ((num_class1 // 2) + 1)

if num_class2 % 2 == 0:
  desks = desks + (num_class2 / 2)
else:
  desks = desks + ((num_class2 // 2) + 1)

if num_class3 % 2 == 0:
  desks = desks + (num_class3 / 2)
else:
  desks = desks + ((num_class3 // 2) + 1)

print(int(desks))