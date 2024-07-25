#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 041")
# Ask the user to enter their name and a number. If the number is less than 10, then display
# their name that number of times; otherwise display the message "Too high" three times.

name = input("Enter your name: ")
num = int(input("Enter a number: "))

if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print("Too high!")
