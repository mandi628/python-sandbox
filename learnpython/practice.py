# Practice problems from learnpython.org website.

print("This line will be printed.")

x = 1
if x == 1:
    print("x is 1.")

print("Goodbye, World!")
print("Hello, World!")

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
# The difference between the two is that apostrophes would terminate the string.
mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
# Assignments can be done on more than one variable "simultaneously" on the same line
a, b = 3, 4
print(a, b)

# Mixing operators between numbers and strings is not supported. This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

# However, converting the numbers to strings by adding quotes will work.
one = "1"
two = "2"
three = "hello"

print(one + " " + two + " " + three)

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

# Accessing an index which does not exist generates an exception (an error).
print(mylist[10])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Arithmetica Operators
number = 1 + 2 * 3 / 4.0
print(number)

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. divident % divisor = remainder.
remainder = 11 % 3
print(remainder)

# Two multiplication symbols akes the power relationship
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Python supports concatenating strings using the addition operator
helloworld = "hello" + " " + "world"
print(helloworld)

# Python also supports multiplying strings to form a string with a repeating sequence
lotsofhellos = "hello " * 10
print(lotsofhellos)

# Join lists with the addition operators
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

# Create two lists called x_list and y_list which contain 10 instances of the variable x and y. You also will create a big_list which contains the variables x and y 10 times each, by concatenating the two lists you have created.
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x-list))
print("y_list contains %d objects" % len(y-list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
# The code above worked on the web module, but does not seem to work here. Not sure why it is not liking the object assignments in lines 1 & 2, but it is not recognizing the assignment of x & y as objects. And yet, the testing code worked. Hmmm...

name = "John"
age = 23
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))

mylist = [1, 2, 3]
print("A list: %s" % mylist)

"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>.f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""

# Exercise: Write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)