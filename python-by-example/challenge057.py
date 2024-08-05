#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 057")

# Update program 056 so that it tells the user if they are too high or 
# too low before they pick again.

import random

num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != num:
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    guess = int(input("Guess again: "))

print("You got it!")

""" Solution in book:
import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
"""
