#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 006")
# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format.
pizza = int(input("How many slices of pizza did you start with? "))
eaten = int(input("How many slices of pizza have you eaten? "))
left = pizza - eaten
print("You have", left, "slices left.")
