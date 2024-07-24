# Get Programming: Learn to Code in Python, by Ana Bell
# Borrowed from library 2024.07.05
# mandi628.codes@gmail.com

# Unit 3: Making Decisions in Your Programs
# Lesson 14: Making More Complicated Decisions

print("Listing 13.3")
num_a = int(input("Pick a number: "))
if num_a > 0:
    print("Your number is positive") # After this, the code continues to 
	# to check against the next conditional
if num_a < 0:
    print("Your number is negative")
if num_a == 0:
    print("Your number is zero")
print("Finished")

print("--------")

print("Listing 14.4")
num_b = int(input("Enter a number: "))
if num_b > 0:
    print("Your number is positive")
elif num_b < 0:
    print("Your number is negative")
else:
    print("Your number is zero")
# This format causes the program to go to the end, instead of resuming
# the series of conditionals.

print("\n~~~~~~~~\n")

print("Quick check 14.6")
num = int(input("Enter a number: "))
# With if-elif-else statements
if num < 6: # If true, print statement, then go to end. If false, go to next
    print("num is less than 6")
elif num < 10: # If true, print, then end. If false, go to next.
    print("num is less than 10")
elif num > 3: # If true, print, then end. If false, go to next.
    print("num is greater than 3")
else: # If above are false, print, then end.
    print("No relation found.")
print("Finished")

print("--------")

# With if statements:
if num < 6: # If true, print, then next. If false, then next.
    print("num is less than 6")
if num < 10: # If true, print, then next. If false, then next.
    print("num is less than 10")
if num > 3: # If true, print, then next. If false, the next.
    print("num is greater than 3")
print("Finished")

print("\n~~~~~~~~\n")

print("Q14.1 - Number Comparison")
# Write a program that reads in two numbers from the user. The program 
# should print the relation between the two numbers, which will be one of 
# the following:
# - numbers are equal
# - first number is less than the second number
# - first number is greater than the second number

num_c = input("Please enter a number: ")
num_d = input("Please enter another number: ")
if int(num_c) == int(num_d):
    print("Your numbers are equal.")
elif int(num_c) < int(num_d):
    print("Your first number is less than your second number.")
elif int(num_c) > int(num_d):
    print("Your first number is greater than your second number.")
else:
    print("You didn't follow directions.")
print("Thank you for playing!")

print("\n~~~~~~~~\n")

print("Q14.2 - Vowel Hunt")
# Write a program that reads in a string from the user. If the string
# contains at least one of every voel (a, e, i, o, u), print "You have
# all the vowels!" Additionally, if the string starts with the letter
# a and ends with the letter z, print "And it's sort of alphabetical!"

string = input("Enter a phrase or sentence: ")
string_lower = string.lower()
if "a" in string_lower = True:
    print("There are A's")
if "e" in string_lower = True:
    print("There are E's")
if "i" in string_lower = True:
    print("There are I's")
if "o" in string_lower = True:
    print("There are O's")
if "u" in string_lower = True:
    print("You have all the vowels!") 
