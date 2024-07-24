#! /usr/bin/env python

# Get Programming: Learn to Code with Python, Ana Bell
# borrowed from library 2024-07-05

# Unit 5: Organizing Your Code into Reuseable Blocks
# Lesson 22: Advanced operations with functions

print("Lesson 22, Q-1")
# Fill the missing parts to the following code:
def area(shape, n):
    # write a line to return the area
    # of a generic shape with a parameter of n
    return shape(n)

def circle(radius):
    return 3.14*radius**2

def square(length):
    return length*length

print("The area of a circle with the radius of 5: ", area(circle, 5)) #example function call

# Write a line to use area() to find the area of a circle with a radius of 10
print("The area of a circle with the radius of 10: ", area(circle, 10))

# Write a line to use area() to find the area of a square with sides of length 5
print("The area of a square with a side of 5: ", area(square, 5))

# Write a line to use area() to find the area of a circle with the diameter of length 4
print("The area of a circle with a diameter of 4: ", area(circle, 2))

# BONUS: Write the code necessary to receive input from the user, asking whether it's
#    a circle or square, and what the dimension is, then print the result.
print("--------")
print("Please use ALL CAPS for your responses.")
my_shape = input("Enter either SQUARE or CIRCLE: ")

if my_shape == "SQUARE":
    my_length = int(input("Enter the length of one of the sides: "))
    print("The area of a square with a side of", my_length, ": ", area(square, my_length))
elif my_shape == "CIRCLE":
    my_rad = int(input("Enter the length of the radius: "))
    print("The area of a circle with a radius of", my_rad, ": ", area(circle, my_rad))
else:
    print("I'm sorry. I can't do that right now.")

print("\n~~~~~~~~\n")

print("Lesson 22, Q-2")
# Fill the missing parts to the following code:
def person(age):
    print("I am a person")
    def student(major):
        print("I like learning")
        def vacation(place):
            print("But I need to take a breaks")
            print(age, "|", major, "|", place)
        # write a line to return the appropriate function
        return vacation
    # write a line to return the appropriate function
    return student

# For example, the function call
person(12)("Math")("beach") #example function call

# should print this:
# I am a person
# I like learning
# But I need to take breaks
# 12 | Math | beach
print("- - - - -")
# Write a function call with age of 29, major of "CS", and vacation place of "Japan"
person(29)("CS")("Japan")
print("- - - - -")
# Write a function call so that the last line of its printout is as follows:
#    23 | "Law" | "Florida"
person(23)("Law")("Florida")
print("- - - - -")
# BONUS: Write the code necessary to prompt the user for the answers to the text, then
#    print the result.
print("--------")
my_age = input("Enter your age: ")
my_maj = input("Enter your major: ")
my_vac = input("Enter your fave vacay spot: ")
print("\n")
person(my_age)(my_maj)(my_vac)
