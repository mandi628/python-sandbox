#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 055")

# Randomly choose a number between 1 and 5. Ask the user to pick a number.
# If they guess correctly, display the message "Well done", otherwise
# tell them if they are too high or too low and ask them to pick a second
# number. If they guess correctly on their second guess, display "Correct",
# otherwise display "You lose"

import random

num = random.randint(1,5)
pick = int(input("Choose a number between 1 and 5: "))

if pick == num:
    print("Well done.")
elif pick > num:
    print("Too high.")
    pick = int(input("Guess again: "))
    if pick == num:
        print("Correct.")
    else:
        print("You lose.")
elif pick < num:
    print("Too low.")
    pick = int(input("Guess again: "))
    if pick == num:
        print("Correct.")
    else:
        print("You lose.")


