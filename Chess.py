x_col = int(input())
y_row = int(input())
num_moves = 0

if (0 < x_col <= 8 and 0 < y_row <= 8):
    for i in range(x_col - 1, x_col + 2):
        if 1 <= i <= 8:
            for j in range(y_row - 1, y_row + 2):
                if (j != y_row or i != x_col):
                    if 1 <= j <= 8:
                        num_moves += 1                

print(num_moves)
