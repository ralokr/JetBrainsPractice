shelf = []
n = int(input())
books_read = []

for _ in range(0, n):
    choice = input()
    if "BUY" in choice:
        action = choice.split(" ", 1)[0]
        book_name = choice.split(" ", 1)[1]
    elif choice == 'READ':
        action = choice

    if action == 'BUY':
        shelf.append(book_name)
    elif action == 'READ':
        books_read.append(shelf[-1])

for i in books_read:
    print(i)
