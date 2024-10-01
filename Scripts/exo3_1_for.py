# Given the following list

animal_list = ['cow', 'mouse', 'yeast', 'bacteria']

# Extract the length of the animal_list with len(list) function
# and stock result in length_animal_list variable

length_animal_list = len(animal_list)

print(f"La taille de mon tableau est de : {length_animal_list}")

# using while to list animal_list content

for indice, animal in enumerate(animal_list):
    print(indice, animal)