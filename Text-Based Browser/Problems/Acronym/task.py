# read test.txt
file = open('test.txt', 'r')

for i in file:
    print(i[0])

file.close()