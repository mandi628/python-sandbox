#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 036")
# Alter program 035 so that it will ask the user to enter their name and a number and then 
# display their name that number of times.

name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(1, num+1):
    print("%s, %d" % (name, i))
