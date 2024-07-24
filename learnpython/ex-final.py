# learnpython.org - Hello World!
print("__Hello World!__")
print("Hello, World!")

# learnpython.org - Variables and Types
# Create a string, an integer, and a floating point number. The string should be named
# mystring and should contain the word "hello". The floating point number should be named
#  myfloat and should contain the number 10.0, and the integer should be names myint and
# should contain the number 20.
print("__Variables and Types__")
mystring = "hello"
myfloat = 10.0
myint = 20

#testing code
if mystring == "hello":
	print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
	print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
	print("Integer: %d" % myint)

# learnpython.org - Lists
# Add numbers and strings to the correct lists using the "append" list methond.
# You must add the numbers 1, 2, and 3 to the "numbers" list, and the words 'hello' and
# 'world' to the strings variable.

# You will also have to fill in the variable second_name with the second name in the names
# list, using the brackets operator []. Note that the index is zero-based, so if you want to 
# access the second item in the list, its index will be 1.
print("__Lists__")
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = []
strings.append('hello')
strings.append('world')
names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s." % second_name)

# learnpython.org - Basic Operators
# The target of this exercise is to create two lists called x_list and y_list, which contain
# 10 instances of the variables x and y, respectively. You are also required to create a list
# called big_list, which contains the variables x and y, 10 times each, by concatenating the
# two lists you have created.
print("__Basic Operators__")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
	print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
	print("Great!")

# learnpython.org - String Formatting
# Write a format string which print out the data using the following sytax: "Hello John
# Doe. Your current balance is $53.44.
print("__String Formatting__")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# learnpython.org - Basic String Operations
# Try to fix the code to print out the correct information by changing the string.
print("__Basic String Operations__")
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" % s[1::2]) # (0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())
# Convert evertying to lowercase
print("String in lowercase: %s" % s.lower())
# Check how a string starts
if s.startswith("Str"):
	print("String starts with 'Str'. Good!")
# Check how a string ends
if s.endswith("ome!"):
	print("String ends with 'ome!'. Good!")
# Split the string into three separate strings, each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# learnpython.org - Conditions
print("__Conditions__")
# Change the variables in the first section, so that each if statement resolves as True.
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
	print("1")
if first_array:
	print("2")
if len(second_array) == 2:
	print("3")
if len(first_array) + len(second_array) == 5:
	print("4")
if first_array and first_array[0] == 1:
	print("5")
if not second_number:
	print("6")

# learnpython.org - Loops
# Loop through and print out all even numbers from the numbers list in the same order
# they are received. Don't print any numbers that come after 237 in the sequence.
print("__Loops__")
numbers = [
	951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
	615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
	386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
	399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
	815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
	958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
	743, 527
]

for number in numbers:
	if number == 237:
		break
	if number % 2 == 1:
		continue
	print(number)

# learnpython.org - Functions
# In this exercise you'll use an existing function, and while adding your won to create
# a fully functional program.

# 1. Add a function name list_benefits() that returns the following list of strings:
# "More organized code," "More readable code", " Easier code reuse", "Allowing programmers
# to share and connect code together"

# 2. Add a function named build_sentence(info) which receives a single argument containing
# a string and returns a sentence starting with the given string and ending with the string
# " is a benefit of functions!"

# 3. Run and see all the functions work together!
print("__Functions__")
# Modify this function to return a list of strings as defined above
def list_benefits():
	return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
# Modify this function to concatenate to each benefit - "is a benefit of functions!"
def build_sentence(benefit):
	return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
	list_of_benefits = list_benefits()
	for benefit in list_of_benefits:
		print(build_sentence(benefit))

name_the_benefits_of_functions()

# learnpython.org - Classes and Objects
# Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth
# $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
print("__Classes & Objects__")
# define the Vehicle class
class Vehicle():
	name = ""
	kind = "car"
	color = ""
	value = 100.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind,
			self.value)
		return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

car3 = Vehicle()
car3.name = "Masha"
car3.kind = "sedan"
car3.color = "black"
car3.value = 9500.00

car4 = Vehicle()
car4.name = "Pandora"
car4.kind = "SUV"
car4.color = "gray"
car4.value = 400.00

print(car1.description())
print(car2.description())
print(car3.description())
print(car4.description())

# learnpython.org - Dictionaries
print("__Dictionaries__")
# Using a phonebook created with the dictionary format, add "Jake" to the phonebook
# with phone number 938273443, and remove Jill from the phonebook.
phonebook = {
	"John" : 938477566,
	"Jack" : 938377264,
	"Jill" : 947772781
}
print("Phonebook v1: %s" % phonebook)
# your code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
print("Phonebook v2: %s" % phonebook)
# testing code
if "Jake" in phonebook:
	print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
	print("Jill is not listed in the phonebook.")

# learnpython.org - Modules & Packages
# Print an alphabetically sorted list of all the functions in the re module containing
# the word find.
print("__Modules & Packages__")
import re
find_members = []
for member in dir(re):
	if "find" in member:
		find_members.append(member)

print(sorted(find_members))

# learnpython.org - Numpy Arrays
print("__Numpy Arrays__")
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_weight_kg = np.array(weight_kg)

np_weight_lbs = np_weight_kg * 2.2
print("Numpy weight in lbs: %s" % np_weight_lbs)
