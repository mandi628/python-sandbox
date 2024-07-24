#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 019")
# As the user to enter 1, 2, or 3. If they enter a 1, display the message
# "Thank you", if they enter a 2, display "Well done", if they enter a 3
# display "Correct". If they enter anything else, display "Error message".
a = input("Please enter 1, 2, or 3: ")

if a == "1":
    print("Thank you")
elif a == "2":
    print("Well done")
elif a == "3":
    print("Correct")
else:
    print("Error message")
