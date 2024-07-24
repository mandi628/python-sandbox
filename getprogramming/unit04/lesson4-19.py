# Get Programming: Learn to Code with Python, Ana Bell
# borrowed from library 2024.07.05

# Unit 4: Repeating tasks
# Lesson 19: Capstone: Scrabble, Art Edition

# Write a program that can tell you words that you can form from a set of tiles;
# the set of all valid words is a subset of all the English words (in this case,
# only words related to art). When dealing with chooseing the best word from
# the given tiles, here are some details to remember:

# ~ All valid words related to art are given to you as a string, each word
#    separated by a newline. The string organizes the words by length, shortest
#    to longest. All valid words contain only letters in the alphabet (no
#    spaces, hyphens, or special symbols).

# ~ The number of tiles you get can vary, it's not a fixed number.

# ~ Letters on tiles don't have point values; they're all worth the same.

# ~ The tiles you get are given as a string. For example, tiles = "hijklmnop"

# ~ Report all valid words you can form with your tiles in a tuple of strings, for
#    example, ('ink', 'oil', 'kiln')

words = "art\nhue\nink\noil\npen\nwax\nclay\ndraw\nfilm\nkiln\npastel\nshading\nwatercolor\ncrosshatching\n"
tiles = input("Enter your tiles: ")

all_valid_words = () #empty tuple for valid words

start = 0
end = 0

found_words = () #empty tuple for found words

for char in words:
    if char == "\n":
        all_valid_words = all_valid_words + (words[start:end],) #Add singleton tuple to current all valid words tuple
        start = end + 1 # Sets the start counter to the next char
        end = end + 1
    else:
        end = end + 1

# Making a valid word with the given tiles

# Given the valid words and a set of tiles, start with the first valid word and
#    check whether all its letters are in the set of tiles. If so, add it to the
#    set of words you can make. If at least one letter is in a valid word but
#    not in the tiles, you can't make the word.

for word in all_valid_words:
    tiles_left = tiles
    for letter in word:
        if letter not in tiles:
            break
        else:
            index = tiles_left.find(letter) # Finds position of letter in tiles_left
            tiles_left = tiles_left[:index] + tiles_left[index+1:] #Removes letter and makes a new tiles_left
    if len(word) == len(tiles) - len(tiles_left):
        found_words = found_words + (word,)
print(found_words)
