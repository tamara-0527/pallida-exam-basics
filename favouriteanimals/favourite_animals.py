# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

from sys import argv





def add_fav_animals():
    fav_animals = 'favourites.txt'
    animal = argv[-1]
    with open(fav_animals, 'r+') as fav_animals:
        for line in fav_animals:
            if animal in fav_animals:
                return "It's existed"
            elif animal not in fav_animals:
                fav_animals.write(''.join(animal) + '\n')
                return fav_animals

def controller():
    if argv[-1] == "favourite_animals.py":
        return ("fav_animals [animal] [animal]")
    else:
        return add_fav_animals()

    
print(controller())