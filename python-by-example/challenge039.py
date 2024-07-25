#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 039")
# Ask the user to enter a number between 1 and 12 and then display the times table for that
# number.

num = int(input("Enter a number between 1 and 12: "))

for x in range(1, 13):
    answer = x * num
    print(x, " * ", num, " = ", answer)
