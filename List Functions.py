lucky_numbers = [1, 5, 3]

friends = ["Monica", "Alok", "Ankit"]

print(friends)

friends.extend(lucky_numbers)

print(friends)

lucky_numbers.extend(friends)

print(lucky_numbers)

friends.append("Casey")		# Appends elements to the end of the list

print(friends)

# Inserts elements at a specified position(index) in the list
friends.insert(2, "Apple")

print(friends)

friends.remove("Ankit")

print(friends)

friends.clear()		# Removes all elements from the list

print(friends)

friends.append("Casey")
friends.pop()

print(friends)

friends.append("Toby")

print(friends)

print(friends.index("Toby"))

friends.append("Toby")

print(friends.count("Toby"))

friends.append("Michael")

print(friends)

friends.sort()

print(friends)

# Not a reverse sort; this function just reverses the order
# the list elements are in
friends.reverse()

print(friends)

friends2 = friends.copy()

print(friends2)
