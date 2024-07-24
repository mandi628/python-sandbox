# Get Programming: Learn to Code in Python, by Ana Bell
# Borrowed from library 2024.07.06

# Unit 2: Strings, Tuples, and Interacting With the User
# Leson 11: Interacting With the User

print("Quick check 11.1")
print(13-1)
"nice"
a = "nice"
b = " is the new cool"
print(a.capitalize() + b)

print("\n~~~~~~~~\n")

print("Quick check 11.2")
#Initialize variables
a = 1
b = 2
c = a/b #Calculates the division
print(a,"/",b,"=",c) #Uses commas to separate the integers and the strings
add = str(a)+"/"+str(b)+"="+str(c) #Converts ints to strings, then concatenates
print(add)

print("\n~~~~~~~~\n")

sweet = "cookies"
savory = "pickles"
num = 100
print(str(num) + " " + sweet + " and " + str(num) + " " + savory)
print("I choose the " + sweet.upper() + "!")

print("\n~~~~~~~~\n")

print("Quick check 11.3")
secret = input("Tell me a secret: ")
color = input("What is your favorite color? ")
char = input("Enter one of the following: #, $, %, &, or *. ")
print("I won't tell your secret, but your favorite color is " + color + "and you picked " + char + ".")

print("\n~~~~~~~~\n")
print("Quick check 11.4")
#Ask the user for the name of their favorite song. Then print the name
#  of the song three times, on separate lines.
song = input("What is your favorite song? ")
song_title = song.upper()
print((song_title + "\n") * 3)
# Ask the user for a celebrity's first and last name. Then print the first
# name on one line and the last name on another line.
name = input("Give a celebrity's first and last name: ")
split = name.find(" ")
first_name = name[:split]
last_name = name[split+1:]
print(first_name.capitalize() + "\n" +  last_name.capitalize())

print("\n~~~~~~~~\n")

print("Quick check 11.5")
# Modify the program given so that the output printed to the console is
# a decimal number.
user_input = input("Enter a number to find the square of: ")
num = int(user_input)
print(num * num)
ber = float(user_input)
print(ber * ber)

print("\n~~~~~~~~\n")

print("Q11.1")
# Write a program that asks the user for two numbers. Store these numbers
# in variables b and e. The program calculates and prints the power b^e
# with an appropriate message.
b = int(input("Enter a number: "))
e = int(input("Enter another number: "))
a = b ** e
print("The result of %d to the power of %d is: %s" % (b, e, a))

print("--------")

print("Q11.2")
# Write a program that asks the user's name and then age. Use appropriate
# variable names to store these variables. Calculate how old the user will
# be in 25 years. For example, if the user enter Bob and 10, the program
# should print Hi Bob! In 25 years you will be 35!
name = input("What is your name? ")
age = input("How old are you? ")
older = int(age) + 25
print("Hi, %s! In 25 years, you will be %d!" % (name, older))
