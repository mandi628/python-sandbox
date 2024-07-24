#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 033")
# Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out
# the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 2 display 7 divided by 2 is 3
# with 1 remaining).

num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter another whole number: "))

div = num1 // num2
rem = num1 % num2

print("You enter %d and %d." % (num1, num2))
print("%d divided by %d is %d with %d remaining." % (num1, num2, div, rem))
