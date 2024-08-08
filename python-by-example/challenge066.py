#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 066")

# Draw an octagon that uses a different colour (randomly selected
# from a list of six possible colours) for each line.

import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0,8):
    turtle.color(random.choice(colors))
    turtle.forward(100)
    turtle.left(45)

turtle.exitonclick()
