'''
This program finds all numbers in the range (a,b)
that are divisible by 3. It then calculates their mean.
'''

a = int(input())
b = int(input())
total = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        counter += 1
        total += i

print(total / counter)
