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


fav_animals = 'favourites.txt'

def add_fav_animals(fav_animals, animal):
    with open(fav_animals, 'a') as f:
        if animal not in file_name:
            fw.write(''.join(animal) + '\n')
        else:
            return False


def controller():
    if argv[-1] == "favourite_animals.py":
        return ("fav_animals [animal] [animal]")
    

print(controller())