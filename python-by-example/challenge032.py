#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 032")
# Ask for the radius and the depth of a cylinder and work out the total volume (circle area * depth), rounded to three decimal places.

import math

rad = float(input("Enter the radius of your cylinder: "))
dep = float(input("Enter the depth of your cylinder: "))

area = (2 * rad) * math.pi
vol = area * dep

print("The volume of your cylinder is %s." % round(vol, 3))
