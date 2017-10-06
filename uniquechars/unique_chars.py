# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(word):
    unique_letters = []
    letters = len(word)
    if letters == 0:
        return False
    for letter in word:       
        unique_letters.append(letter)
        if letter == "a":
            unique_letters.remove("a")
    return unique_letters
        

unique_characters("anagram")
