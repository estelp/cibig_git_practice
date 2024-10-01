# Given the following kist of odd numbers

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Declare a new empty list

events = []

# Create a new variable indice start by 0

for indice, number in enumerate(odds):
    print(indice, number)
    value = int(number + 1)
    events.append(value)

print(events)