def printCells():
  line_text = ''
  separator = '|'
  print('---------')

  for i in range(0,len(cells)):
    if i % 3 == 0:
      line_text = line_text + ' ' + cells[i]
      line_text = separator + line_text
    elif ((i+1) % 3) == 0:
      line_text = line_text + ' ' + cells[i] + ' ' + separator
      print(line_text + '\n')
      line_text = ''
    else:
      line_text = line_text + ' ' + cells[i]

  print('---------')    

cells = list(input())

num_X = 0
num_O = 0
num_blank = 0
winner_X = False
winner_O = False
noErrors = False

if len(cells) < 9:
  for j in range(len(cells),9):
    cells.append('_')
else:
  while len(cells) > 9:
    del cells[-1]

printCells()

for i in range(0,len(cells)):
  if cells[i] == 'X':
    num_X += 1
  elif cells[i] == 'O':
    num_O += 1
  else:
    num_blank += 1

while not noErrors:
  next_move = input("Enter the coordinates: ").split(" ")

  if len(next_move) > 2:
    print("Too many coordinates!")
    continue

  if len(next_move) < 2:
    print("Too less coordinates!")  
    continue

  if not(next_move[0].isnumeric()) or  not(next_move[1].isnumeric()):
    print("You should enter numbers!")
    continue

  pos_x = int(next_move[0])
  pos_y = int(next_move[1])


  if pos_x not in [1,2,3] or pos_y not in [1,2,3]:
    print("Coordinates should be from 1 to 3!")
    continue

  pos_cell = 0

  if pos_x == 1:
    if pos_y == 1:
      pos_cell = 6
    elif pos_y == 2:
      pos_cell = 3
    elif pos_y == 3:
      pos_cell = 0
  elif pos_x == 2:
    if pos_y == 1:
      pos_cell = 7
    elif pos_y == 2:
      pos_cell = 4
    elif pos_y == 3:
      pos_cell = 1
  elif pos_x == 3:
    if pos_y == 1:
      pos_cell = 8
    elif pos_y == 2:
      pos_cell = 5
    elif pos_y == 3:
      pos_cell = 2    

  if cells[pos_cell] != '_':
    print("This cell is occupied! Choose another one!")
    continue  
  else:
    cells[pos_cell] = 'X'
    printCells()
    noErrors = True
