# Given the following list

animal_list = ['cow', 'mouse', 'yeast', 'bacteria']

# Create a new variable indice start by 0

indice = 0

# Extract the length of the animal_list with len(list) function
# and stock result in length_animal_list variable

length_animal_list = len(animal_list)

print(f"La taille de mon tableau est de : {length_animal_list}")

# using while to list animal_list content

while indice < length_animal_list:
    print(f"--------- Mon indice est : {indice}")
    print(f"Mon element lu est : {animal_list[indice]}\n")
    indice = indice + 1