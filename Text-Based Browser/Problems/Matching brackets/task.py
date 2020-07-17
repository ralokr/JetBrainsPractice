x = input()
is_error = False

bracket_store = []

for i in x:
    if i == '(':
        bracket_store.append(i)
    elif i == ')':
        try:
            bracket_store.pop()
        except IndexError:
            is_error = True

if is_error or bracket_store != []:
    print("ERROR")
else:
    print("OK")