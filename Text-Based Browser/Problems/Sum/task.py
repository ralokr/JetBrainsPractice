# read sums.txt
file = open('sums.txt', 'r')

for i in file:
    x, y = i.split(" ")
    result = int(x) + int(y)
    print(result)

file.close()