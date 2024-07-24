#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 018")
# Ask the user to enter a number. If it is under 10, display the message "Too low",
# if their number is between 10 and 20, display "Correct", otherwise display "Too
# high."
num = int(input("Enter a number: "))

if num < 10:
    print("Too low.")
elif num > 20:
    print("Too high.")
else:
    print("Correct!")
