#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 065")

# Write the numbers as shown below, starting at the bottom of the number one.
# (Picture is digital style numbers 1, 2, & 3.)

import turtle

turtle.penup()
turtle.left(180)
turtle.forward(200)

turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.penup()

turtle.right(90)
turtle.forward(100)

turtle.pendown()
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.penup()

turtle.forward(100)

turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(150)

turtle.exitonclick()
