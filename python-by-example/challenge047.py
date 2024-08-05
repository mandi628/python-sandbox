#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 6: While Loop

print("Challenge 047")

# Ask the user to enter a number and then enter another number. Add these
# two numbers together and then ask if they want to add another number.
# If they enter "y", ask them to enter another number and keep adding
# numbers until they do not answer "y". Once the loop has stopped, display
# the total.

num1 = int(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
    num_x = int(input("Enter your next number: "))
    total = total + num_x
    print("Your total is", total)
    again = input("Do you want to add another number? (y/n) ")
print("Your final total is", total)
