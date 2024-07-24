#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 028")
# Update program 027 so that it will display the answer to two decimal places.

num = float(input("Enter a number with a lot of decimal places:\n:: "))

print("Your number times 2 and rounded to 2 decimals is: ", round(num * 2, 2))

print("\n~~~~~~~~\n")

print("Challenge 028 - v2")

num1 = float(input("Enter a number with a lot of decimal places:: "))

num2 = int(input("Enter a whole number:: "))

print("Your number times", num2, "and rounded to 2 decimals is: ", round(num1 * num2, 2))
