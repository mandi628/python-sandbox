#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 011")
# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number
# in a user-friendly format.
big = int(input("Enter a number over 100: "))
lil = int(input("Enter a number under 10: "))
gz = int(big / lil)
rem = big % lil
print(lil, "goes into", big, gz, "times, with", rem, "left over.")
