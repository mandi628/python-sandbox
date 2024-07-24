#Get Programming: Learn to Code with Python, by Ana Bell
#borrowed from library 2024-07-05

#Unit 4: Repeating tasks
#Lesson 17: Customizing Loops

print("Quick check 17.1")
for i in range(0,9):
    print("The range(0.9): ", i)
print("--------")
for j in range(3,8):
    print("The range(3,8): ", j)
print("--------")
for k in range(-2,3,2):
    print("The range(-2,3,2): ", k)
print("---------")
for m in range(5,-5,-3):
    print("The range(5,-5,-3): ", m)
print("--------")
for p in range(4,1,2):
    print("The range(4,1,2): ", p)
print("Range(4,1,2) prints nothing because the start & stop terms are backwards.")

print("\n~~~~~~~~\n")

print("Quick check 17.2")
# Write a piece of code that asks the user for input. Then write a loop that iterates over every characher.
# The code prints "vowel" every time it encounters a vowel character.

vowels = "aeiou"
string = input("Enter a string: ")
for w in string:
    if w in vowels:
        print("vowel")
        continue
    print(w)

print("\n~~~~~~~~\n")

print("Q17.1 - Evens and 6's")
# Write a program that iterates over all even numbers between 1 and 100.
# If the number is also divisible by 6, increment a counter.
# At the end of your program, print how many numbers are even and also divisible by 6.

even = 0
six = 0
for i in range(1,101):
    if i % 2 == 0:
        even += 1
    if i % 6 == 0:
        six += 1
print("Even numbers between 1 and 100: ", even)
print("Numbers between 1 and 100 divisible by 6: ", six)
print("------\nBook version")
counter = 0
for num in range(2,100,2):
    if num % 6 == 0:
        counter += 1
print(counter, "numbers are even and devisible by 6")

print("\n~~~~~~~~\n")

print("Q17.2 - 99 bottles of beer")
n = int(input("Enter a number: "))
for n in range(n,0,-1):
    print("Alice's camel has ", n, "humps, \n Alice's camel has ", n, "humps. \n Alice's camel has ", n, "humps, so go, Alice, go.")
    n -= 1
if n == 0:
    print("Alice's camel has no humps, \n Alice's camel has no humps, \n Alice's camel has no humps. Flat as a horse!")

print("--------")

print("Book version")
count = int(input("How many books on Python do you have? "))
for n in range(count,0,-1):
    if n == 1:
        print(n, "book on Python on the shelf", n, "book on Python")
        print("Take one down, pass it around, no more books!")
    else:
        print(n, "books on Python on the shelf", n, "books on Python")
        print("Take one down, pass it around,", n-1, " books left.")

print("\n~~~~~~~~\n")

print("Q17.3")
# Write a program that asks the user to input names separated by a single space.
# Your program should print a greeting for every name entered, separated by a new line.
names = input("Enter some names, separated by a space: ") # Had to use the book answer
name = ""
for x in names:
    if x == " ": # Iterates through string, and stops at space
        print("Hi", name) # Prints the iteration to the space
        name = "" # Resets the variable to continue through the string
    else:
        name += x # Tells the loop to keep going to the next character
# Since the last name doesn't have a space, we have to treat it differently
lastspace = names.rfind(" ") # Use reverse find the find the space from the end
print("Hi", names[lastspace+1:]) # Prints the string forward from the last space
