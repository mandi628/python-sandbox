#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 005")
# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as 'The answer is [answer]'
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("One more number: "))
answer = (x + y) * z
print("The answer is", answer)
