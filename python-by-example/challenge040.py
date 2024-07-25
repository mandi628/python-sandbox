#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 040")
# Ask for a number below 50 and then count down from 50 to that number, making sure you
# show the number they entered in the output.

num = int(input("Enter a number less than 50: "))

for x in range(50, num-1, -1):
    print(x)
