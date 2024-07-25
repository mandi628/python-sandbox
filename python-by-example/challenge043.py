#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 043")
# Ask which direction the user wants to count (up or down). If they select up, then ask
# then for the top number and then count from 1 to that number. If they select down, 
# ask them to enter a number below 20 and then count down from 20 to that number. If they
# entered something other than up or down, display the message "I don't understand."

dir = input("Do you want to count up or down? (u/d) ")

if dir == "up" or dir == "u":
    top = int(input("What is the highest number you want to count? "))
    for i in range(1, top+1):
        print(i)
elif dir == "down" or dir == "d":
    bottom = int(input("Enter a number under 20: "))
    for i in range(20, bottom-1, -1):
        print(i)
else:
    print("I don't understand.")
