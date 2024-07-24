#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 015")
# Ask the user to enter their favourite colour. If they enter "red", "RED" or "Red" display the message
# "I like red, too", otherwise display the message "I don't like [colour], I prefer red."
color = input("What is your favorite color? ")

if color == "red" or color == "RED" or color == "Red":
    print("I like red, too.")
else:
    print("I don't like %s, I prefer red." % str.lower(color))
