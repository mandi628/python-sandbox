#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 062")

# Draw a circle.

import turtle

turtle.shape("classic")

for i in range(0,12):
    turtle.right(30)
    for i in range(0,360):
        turtle.forward(2)
        turtle.right(1)

turtle.exitonclick()

# This version draws 12 interlocking circles
