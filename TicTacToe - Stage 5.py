cells = ["_"] * 9
num_X = 0
num_O = 0
num_blank = 0
winner_X = False
winner_O = False
noErrors = False
last_move = 'X'

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

def Result():
    global winner_X
    global winner_O

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

    if "_" not in cells:
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



printCells()

while "_" in cells and not noErrors:
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
        cells[pos_cell] = last_move
        
        if cells[pos_cell] == 'X':
            num_X += 1
        elif cells[pos_cell] == 'O':
            num_O += 1
        else:
            num_blank += 1
 
        if last_move == 'X':
            last_move = 'O'
        else:
            last_move = 'X'

        printCells()
        Result()
        