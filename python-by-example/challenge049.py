#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 6: While Loop

print("Challenge 049")

# Create a variable called compnum and set the value to 50. Ask the user
# to enter a number. While their guess is not the same as the compnum
# value, tell them if their guess is too low or too high and ask them
# to have another guess. If they enter the same value as compnum,
# display the message "Well done, you took [count] guesses."

compnum = 50
count = 0
guess = int(input("Guess my number: "))
while guess != compnum:
    count += 1
    if guess < compnum:
        print("Too low!")
    elif guess > compnum:
        print("Too high!")
    guess = int(input("Guess again: "))
print("Well done, you took", count, "guesses.")
