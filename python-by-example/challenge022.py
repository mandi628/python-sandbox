#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

print("Challenge 022")
# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
first = input("Enter your first name in lowercase: ")
last = input("Enter your last name in lowercase: ")
first_name = str.title(first)
last_name = str.title(last)
name = first_name + " " + last_name
print(name)
