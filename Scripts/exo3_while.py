# Given the following list

animal_list = ['cow', 'mouse', 'yeast', 'bacteria']

# define variable for number of elements

length_animal_list = len(animal_list)

print(length_animal_list)

# using while to list animal_list content

i = 0
while i < length_animal_list:
    print(f"{i} : {animal_list [i]}")
    i = i + 1
