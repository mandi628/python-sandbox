#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 054")

# Randomly choose either heads or tails ("h" or "t"). Ask the user
# to make their choice. If their choice is the same as the randomly
# selected value, display the message "You win", otherwise display
# "Bad luck" At the end, tell the user if the computer selected
# heads or tails.

import random

comp = random.choice(["h", "t"])
play = input("Choose heads or tails: (h/t) ")

if play == comp:
    print("You win!")
else:
    print("Bad luck.")

if comp == "h":
    print("The computer picked heads.")
else:
    print("The computer picked tails.")
