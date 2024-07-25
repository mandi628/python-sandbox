#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 042")
# Set a variable called total to 0. Ask the user to enter five numbers and after each input
# ask them if they want that number included. If they do, then add the number to the total.
# If they do not want it included, don't add it to the toal. After they have entered all
# five numbers, display the total.

total = 0

for i in range(0,5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number include? (y/n) ")
    if ans == "y":
        total = total + num
print(total)
