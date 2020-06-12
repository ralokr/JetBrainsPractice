chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

money = int(input())
bag = 1
item = ''
full_bag = False

if chicken <= money:
    bag = money // chicken
    item = ' chicken'
    full_bag = True
if goat <= money:
    bag = money // goat
    item = ' goat'
    full_bag = True
if pig <= money:
    bag = money // pig
    item = ' pig'
    full_bag = True
if cow <= money:
    bag = money // cow
    item = ' cow'
    full_bag = True
if sheep <= money:
    bag = money // sheep
    item = ' sheep'
    full_bag = True

if full_bag == True:
  if bag == 0:
    print(str(bag + 1) + item)
  elif (bag >= 2 and item != ' sheep'):
    print(str(bag) + item + 's')
  else:
    print(str(bag) + item)
else:
  print('None')      