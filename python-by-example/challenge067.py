#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 067")

# Create the following pattern.

import turtle
turtle.pensize(5)
for i in range(0,10):
    turtle.right(36)
    for i in range(0,8):
        turtle.forward(100)
        turtle.left(45)

turtle.exitonclick()
