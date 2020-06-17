cells = list(input())
line_text = ''
separator = '|'
num_X = 0
num_O = 0
num_blank = 0
winner_X = False
winner_O = False

if len(cells) < 9:
  for j in range(len(cells),9):
    cells.append('_')
else:
  while len(cells) > 9:
    del cells[-1]

print('---------')

for i in range(0,len(cells)):
  if cells[i] == 'X':
    num_X += 1
  elif cells[i] == 'O':
    num_O += 1
  else:
    num_blank += 1

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

if (cells[0] == cells[1] and cells[1] == cells[2] and cells[2] == 'X'
or cells[3] == cells[4] and cells[4] == cells[5] and cells[5] == 'X'
or cells[6] == cells[7] and cells[7] == cells[8] and cells[8] == 'X'
or cells[1] == cells[4] and cells[4] == cells[7] and cells[7] == 'X'
or cells[0] == cells[4] and cells[4] == cells[8] and cells[8] == 'X'
or cells[2] == cells[4] and cells[4] == cells[6] and cells[6] == 'X'
or cells[0] == cells[3] and cells[3] == cells[6] and cells[6] == 'X'
or cells[2] == cells[5] and cells[5] == cells[8] and cells[8] == 'X'):
  winner_X = True
  
if (cells[0] == cells[1] and cells[1] == cells[2] and cells[2] == 'O'
or cells[3] == cells[4] and cells[4] == cells[5] and cells[5] == 'O'
or cells[6] == cells[7] and cells[7] == cells[8] and cells[8] == 'O'
or cells[1] == cells[4] and cells[4] == cells[7] and cells[7] == 'O'
or cells[0] == cells[4] and cells[4] == cells[8] and cells[8] == 'O'
or cells[2] == cells[4] and cells[4] == cells[6] and cells[6] == 'O'
or cells[0] == cells[3] and cells[3] == cells[6] and cells[6] == 'O'
or cells[2] == cells[5] and cells[5] == cells[8] and cells[8] == 'O'):
  winner_O = True

if abs(num_X - num_O) >= 2:
  print('Impossible')
elif winner_X == True and winner_O == True:
    print('Impossible')
elif bool(winner_X) != bool(winner_O):  # XOR operation
  if winner_X == True:
      print('X wins')
  elif winner_O == True:
      print('O wins')
elif num_blank == 0 and not(winner_X == True or winner_O == True):
    print('Draw')
else:
    print('Game not finished')