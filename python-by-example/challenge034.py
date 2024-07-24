#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 4: Maths

print("Challenge 034")
# Display the following message: 1) Square 2) Triangle \n Enter a number:  If the user enters 1, then it should ask them
# for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the
# triangle and display the area. If they type in anything else, it should give them a suitable error message.

import math

select = input("1) Square\n2) Triangle\n3) Rectangle\n4) Circle\n\nSelece your shape (1, 2, 3 or 4): ")

if select == "1":
    len = int(input("Enter the length of one of the sides: "))
    s_area = len ** 2
    print("The area of your square is", round(s_area, 1))
elif select == "2":
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height: "))
    t_area = (base * height) / 2
    print("The area of your triangle is", round(t_area, 1))
elif select == "3":
    width = int(input("Enter the width: "))
    high = int(input("Enter the height: "))
    r_area = width * high
    print("The area of your rectangle is", round(r_area, 1))
elif select == "4":
    rad = int(input("Enter the radius: "))
    c_area = (2 * rad) * math.pi
    print("The area of your circle is", round(c_area, 1))
else:
    print("That is not a valid option. Please try again.")

print("Glad to help. Have a great day!")
