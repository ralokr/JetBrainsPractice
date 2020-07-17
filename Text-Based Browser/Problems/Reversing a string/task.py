n = int(input())

my_stack = []

for _ in range(0, n):
    chars = input()
    my_stack.append(chars)

for _ in range(len(my_stack)):
    print(my_stack[-1])
    my_stack.pop()