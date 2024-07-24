#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 008")
# Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how much each person must pay.
bill = float(input("How much is the bill? $"))
diners = float(input("How many people are dining? "))
each = bill / diners
print(f'Each person must pay ${each:.2f}.') # Advanced notation of f-string to get two decimal places.
# f at the beginning of the function indicates the format, then the text in the SINGLE quotes, the {var:.decf}.
# There are other features, but I don't need them now.
