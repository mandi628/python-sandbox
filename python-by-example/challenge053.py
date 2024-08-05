#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 053")

# Display a random fruit from a list of five fruits.

import random
fruit = ["apple", "banana", "pear", "cantaloupe", "orange"]
print(random.choice(fruit))
