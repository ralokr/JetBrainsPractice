# read sample.txt and print the number of lines
count = 0
file_name = open('sample.txt', 'r')

for i in file_name:
    count += 1
print(count)
file_name.close()
