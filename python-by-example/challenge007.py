#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 007")
# Ask the user for the name and their age. Add 1 to their age and display the output:
# [Name] next birthday you will be [new age].
name = input("What is your name? ")
age = int(input("How old are you? "))
new_age = age + 1
print(name, "on your next birthday, you will be", new_age)
