#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 064")

# Draw a five-pointed star.

import turtle

for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()
