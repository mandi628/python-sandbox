#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 029")
# Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.

import math

num = int(input("Enter a number greater than 500 to find the square root: "))

square = math.sqrt(num)

print("The square root of %s, rounded to 2 decimals, is %s." % (num, round(square, 2)))
