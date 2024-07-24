#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

print("Challenge 021")
# Ask the user to enter their first name and then ask them to enter their surname.
# Join them together with a space between and display the name and the length of the whole name.
first = input("Enter your first name: ")
last = input("Enter your last name: ")
name = first + " " + last
length = len(name)
print("Your full name is", name)
print("The length of your name is", length, "characters.")
print("Without the space, it's %s." % (len(first) + len(last)))
