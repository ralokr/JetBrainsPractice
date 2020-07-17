def range_sum(numbers, start, end):
    total = 0
    for i in range(len(numbers)):
        if int(start) <= int(numbers[i]) <= int(end):
            total += int(numbers[i])
    return total


input_numbers = input().split(" ")
a, b = input().split(" ")
print(range_sum(input_numbers, a, b))