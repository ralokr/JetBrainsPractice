# read animals.txt
old_file = open('animals.txt', 'r')

# and write animals_new.txt
new_file = open('animals_new.txt', 'a')

for i in old_file:
    new_file.write(i.rstrip() + ' ')

new_file.close()
old_file.close()