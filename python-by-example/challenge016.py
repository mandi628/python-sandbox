#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

print("Challenge 016")
# Ask the user if it is raining and convert their answer to lower case so it doesn't matter
# what case they type it in. If they answer "yes", ask if it is windy. If they answer "yes"
# to this second question, display the answer "It is too windy for an umbrella", otherwise
# display the message "Take an umberlla". If they did not answer yes to the first
# question, display the answer "Enjoy your day".
rain = input("Is it raining? ")
raining = str.lower(rain)

if raining == "yes":
    wind = input("Is it windy? ")
    windy = str.lower(wind)
    if windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day!")
