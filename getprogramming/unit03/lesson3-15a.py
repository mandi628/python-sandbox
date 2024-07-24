#! /usr/bin/env python3

# Get Programming: Learn to Code with Python, by Ana Bell
# Borrowed from library 2024.07.05

# Unit 3: Making Decisions in Your Programs
# Lesson 15: Capstone Project: Choose Your Own Adventure
# mandi628.codes@gmail.com

# You'll use conditionals and branching to create a story. At each scene,
# the user will enter a word. The word will tell the program which path
# to continue following. Your program should handle all possible paths
# that the user might choose, but doesn't need to handle any unexpected
# input from the user.

# Setting up the rules
print("Welcome to the Adventure!")
print("You are on a deserted island in a 2D world.")
print("Try to survive until rescue arrives!")
print("Available commands are in CAPITAL letters.") #How to play
print("Any other command exits the game.") #Unexpected behavior
print("First LOOK around...")

do = input(":: ")
if do == "LOOK":
    print("You are stuck in a sand ditch.")
    print("Crawl out LEFT or RIGHT?")

    do = input(":: ")
    if do == "LEFT":
        print("You make it out and see a ship!")
        print("You survived!")
    elif do == "RIGHT":
        print("No can do. That side is very slippery.")
        print("You fall very far into some weird cavern.")
        print("You do not survive.")

else:
    print("You can only do actions shown in capital letters.")
    print("Try again!")
