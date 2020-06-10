x_coordinate = float(input())
y_coordinate = float(input())

if (x_coordinate != 0 or y_coordinate != 0):
    if x_coordinate > 0 and y_coordinate > 0:
            print('I')
    elif x_coordinate > 0 and y_coordinate < 0:
            print('IV')
    if y_coordinate > 0 and x_coordinate < 0:
        print('II')
    elif y_coordinate < 0 and x_coordinate < 0:
        print('III')
                