#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 6: While Loop

print("Challenge 046")

# Ask the user to enter a number. Keep asking until they enter a value over 5
# and then display the message "The last number you entered was a [number]"
# and stop the program.

num = 0
while num <= 5:
    num = int(input("Enter a number: "))
print("The last number you entered was a", num)
