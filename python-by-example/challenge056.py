#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 056")

# Randomly pick a whole number between 1 and 10. Ask the user to enter a
# number and keep entering numbers until they enter the number that was
# randomly picked.

import random

num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != num:
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
"""
