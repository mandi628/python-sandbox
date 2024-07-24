#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 012")
# As for two numbers. If the first one is larger than the second, display the second number first and then the first number.
# Otherwise show the first number first and then the second.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 == num2:
    print(num1, "is equal to", num2)
elif num1 >= num2:
    print(num2, "is less than", num1)
else:
    print(num1, "is less than", num2)
print("Thank you!")
