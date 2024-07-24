# Get Programming: Learn to Code in Python, by Ana Bell
# Borrowed from library 2024.07.05

# Unit 3: Making Decisions in Your Programs
# Lesson 13: Introducing Decisions in Programs

print("Quick check 13.3")
# Ask the user for a word. Print the word that the user gave you. If the
# user gives you input that contains a space, also print that the user
# didn't follow directions.
word = input("Enter a word: ")
word_space = " " in word
if word_space == True:
    print("You didn't follow the directions.")
print(word + "\n")

# Ask the user for two numbers. Print their sum. If the sum is less than
# zero, also print "Wow, negative sum!"
a = input("Enter a number: ")
b = input("Enter another number: ")
c = int(a) + int(b)
if c < 0:
    print("Wow, nagetive sum!")
print(c)

print("\n~~~~~~~~\n")

print("Listing 13.3")
num_a = int(input("Pick a number: "))
if num_a > 0:
    print("Your number is positive")
if num_a < 0:
    print("Your number is negative")
if num_a == 0:
    print("Your number is zero")
print("Finished")

print("\n~~~~~~~~\n")

print("Quick check 13.7 - Chocolate bars")

hungry = input("Are you hungry? (yes or no) ")
price = float(input("How much does a chocolate bar cost? "))

if hungry == "yes":
    if price < 1:
        print("Buy every chocolate bar.")
        bars = 100
    if 1 <= price <= 5:
        print("Buy 10 chocolate bars.")
        bars = 10
    if price > 5:
        print("Buy one chocolate bar.")
        bars = 1
    if bars > 10:
        print("Cashier says: someone's hungry!")

if hungry == "no":
    print("Stick to the list!")

print("\n~~~~~~~~\n")

print("Q13.2")
var = 0
if type(var) == int:
    print("I'm a numbers person.")
if type(var) == str:
    print("I'm a words person.")

print("--------")

print("Q13.3")
text = input("Enter some text: ")
space = text.find(" ")
if space > 0:
    print("This string has spaces.")

print("--------")

print("Q13.4 - Guess my number")
x = int(input("Enter the secret number: (0-9) "))
guess = int(input("Guess my number! (0-9) "))
if guess < x:
    print("Too low!")
if guess > x:
    print("Too high!")
if guess == x:
    print("You got it!")

print("--------")

print("Q13.5 - Absolute value")
num = int(input("Enter a number: "))
if num > 0:
    print("Absolute value: ", num)
if num < 0:
    print("Absolute value: ", -num)
if num == 0:
    print("Absolute value: ", num)
