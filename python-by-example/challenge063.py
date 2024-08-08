#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 8: Turtle Graphics

print("Challenge 063")

# Draw three squares in a row with a gap between each.
# Fill them using three different colors.

import turtle

turtle.penup()
turtle.left(180)
turtle.forward(300)
turtle.right(180)
turtle.pendown()

turtle.begin_fill()
turtle.color("black", "red")
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)

turtle.pendown()
turtle.begin_fill()
turtle.color("black", "yellow")
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)

turtle.pendown()
turtle.begin_fill()
turtle.color("black", "blue")
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()

turtle.exitonclick()
