#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 058")

# Make a maths quiz that asks five questions by randomly generating
# two whole numbers to make the question (e.g. [num1] + [num2]).
# Ask the user to enter the answer. If they get it right add a point
# to their score. At the end of the quiz, tell them how many they got
# correct out of five.

import random

score = 0
for i in range(1,6): # Iterates through 5 random questions
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, "+", num2, "= ")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score += 1
print("You scored", score, "out of 5.")

# I ended up copying from the book for this one. I got the random
# integer part right, but I was setting up each question individually,
# then I realized that it wouldn't generate a new number each time.
# For loops still throw me off, so I would have gotten it wrong.
