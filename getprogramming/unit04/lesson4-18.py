#Get Programming: Learn to Code with Python, by Ana Bell
#borrowed from library 2024-07-05

#Unit 4: Repeating tasks
#Lesson 18: Repeating Tasks While Conditions Hold

print("Listing 18.1")
secret = "code"
guess = input("Guess a word: ")
tries = 1
while guess != secret: # Checks whether the guess is different than the secret word
    print("You tried to guess", tries, "times")
    guess = input("Guess again: ") # Asks the user again
    tries += 1
print("You got it!") # Reached when the guess is correct

print("\n~~~~~~~~\n")

print("Quick check 18.1")
# Write a piece of code that asks the user for a number between 1 and 14. If the user guesses right, print "You guessed right,
# my number was" and then print the number. Otherwise, keep asking for another guess.

number = 12
guess = int(input("Guess a number betwee 1 and 14: "))
while guess != number:
    print("Not it!")
    guess = int(input("Guess again: "))
print("You guessed right, my number was", number)

print("\n~~~~~~~~\n")

print("Quick check 18.2")
# Rewrite the following code with a for loop"
print("Using a while loop:")
password = "robot fort flower graph"
space_count = 0
i = 0
while i < len(password):
    if password[i] == " ":
        space_count += 1
    i += 1
print(space_count)

print("--------")

print("Same code using a for loop:")
password = "robot fort flower graph"
space_count = 0
for ch in password:
    if ch == " ":
        space_count += 1
print(space_count)

print("\n~~~~~~~~\n")

print("Listing 18.4 - Using break")

secret = "code"
max_tries = 100 # Establishes max # of tries
guess = input("Guess a word: ")
tries = 1
while guess != secret:
    print("You tried to guess", tries, "times")
    if tries == max_tries:
        print("You ran out of tries.")
        break # Exits the loop
    guess = input("Guess again: ") # Asks the user again
    tries += 1
if tries <= max_tries and guess == secret: # Gives final message
    print("You got it!")

print("\n~~~~~~~~\n")

print("Quick check 18.3")
# Write a program that uses a while loop to ask the user to guess a secret word of your choosing.
# The user gets 21 tries. When the user gets it right, end the program.
# If the user uses up all 21 tries, exit the loop and print an appropriate message.
secret = "kittens"
max_tries = 21
print("You have 21 tries to guess what I'm thinking.")
guess = input("Guess my word: ")
tries = 1
while guess != secret:
    print("You tried to guess", tries, "times")
    if tries == max_tries:
        print("You ran out of tries. My word was", secret)
        break
    guess = input("Guess again: ")
    tries += 1
if tries <= max_tries and guess == secret:
    print("You got it! Aren't they amazing?")

print("\n~~~~~~~~\n")

print("Q18.1 - Debug")
# This program has a bug. Change one line to avoid the infinite loop.
num = 8
guess = int(input("Guess my number: "))
while guess != num:
    guess = int(input("Guess again: ")) # Added int conversion
print("Right!")

print("\n~~~~~~~~\n")

print("18.2 - Number Guess")

from random import randrange

play = input("Do you want to play a game? ")
while play == "y" or play == "yes":
    number = randrange(10)
    print("I'm thinking of a number between 1 and 10.")
    guess = int(input("What is my number? "))
    while guess != number:
        guess = int(input("Guess again: "))
    print("You got it!")
    play = input("Do you want to play again? ")
print("Ok. Have a great day!")
