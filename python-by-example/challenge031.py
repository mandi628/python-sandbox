#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 031")
# Ask the user to enter the radius of a circle (measurement from the center point to the edge). Work out the area of the circle.

import math

rad = float(input("Enter the radius of a circle: "))

area = (2 * rad) * math.pi

print("The area of the circle is %s." % round(area, 2))
