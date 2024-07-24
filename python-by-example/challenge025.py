#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

print("Challenge 025")
# Ask the user to enter their first name. If the length of their first name
# is under five characters, ask them to enter their surname and join them together
# (without a space) and display the name in upper case. If the length of the first
# name is five or more characters, display their first name in lower case.
first = input("Enter your first name: ")
len_first = len(first)
if len_first < 5:
    last = input("Enter your last name: ")
    name = str.upper(first + last)
    print(name)
else:
    print(str.lower(first))
