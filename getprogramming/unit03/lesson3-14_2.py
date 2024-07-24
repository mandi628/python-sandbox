# Get Programming: Learn to Code in Python, by Ana Bell
# Borrowed from library 2024.07.05
# mandi628.codes@gmail.com

# Unit 3: Making Decisions in Your Programs
# Lesson 14: Making More Complicated Decisions

print("Q14.2 - Vowel Hunt")
# Write a program that reads in a string from the user. If the string
# contains at least one of every voel (a, e, i, o, u), print "You have
# all the vowels!" Additionally, if the string starts with the letter
# a and ends with the letter z, print "And it's sort of alphabetical!"

string = input("Enter a phrase or sentence: ")
string_lower = string.lower()
if "a" in string_lower and "e" in string_lower and "i" in string_lower and "o" in string_lower and "u" in string_lower:
    print("You have all the vowels!") 
if string_lower.startswith("a") and string_lower.endswith("z"):
    print("And it's sort of alphabetical!")
print("See you next time!")
