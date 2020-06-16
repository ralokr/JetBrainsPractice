str_1 = input()
str_2 = input()
str_3 = input()

new_list = []
temp_list = [str_1, str_2, str_3]

for i in range(len(temp_list)):
  for _ in range(i):
    temp_list[i] = [temp_list[i]]
  new_list.append(temp_list[i])

print(new_list)
