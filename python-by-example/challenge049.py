#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 5: For Loop

print("Challenge 044")
# Ask how many people the user wants to invite to a party. If they enter a number below 10,
# ask for the names and after each name display "[name] has been invited." If they enter a
# number which is 10 or higher, display the message "Too many people."

ppl = int(input("How many people do you want to invite to a party? "))

if ppl < 10:
    for i in range(0, ppl):
        name = input("Enter a person's name: ")
        print(name, "has been invited.\n")
    print("Have fun at the party!!!")
elif ppl >= 10:
    print("Too many people.")
