#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 061")

# Draw a triangle.

import turtle

turtle.shape("classic")

for i in range(0,3):
    turtle.forward(150)
    turtle.left(120)

turtle.exitonclick()
