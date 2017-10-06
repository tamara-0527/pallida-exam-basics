# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(word):
    unique_letters = []
    if word == "":
        return False
    if word  == "a":
        unique_letters.append(word)
        return unique_letters

print(unique_characters("a"))
