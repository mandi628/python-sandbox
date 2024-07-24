#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

print("Challenge 023")
# Ask the user to type in the first line of a nursery rhyme and display the length of the string.
# Ask for a starting number and an ending number and then display just that section of the text
# (remember Python starts counting from 0 and not 1).
phrase = input("Enter the first line of a nursery rhyme: ")
print("The length of the string is %s." % len(phrase))
print("For this next part, don't choose a number higher that the string length.")
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
print("The slice is '%s'." % phrase[start:end])
