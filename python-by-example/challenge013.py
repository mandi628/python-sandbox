#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 013")
# Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message "Too high", otherwise diaplay, "Thank you."
num = int(input("Enter a number less than 20: "))

if num >= 20 or num == 20:
    print("Too high!")
else:
    print("Thank you.")
