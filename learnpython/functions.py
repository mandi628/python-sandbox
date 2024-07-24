# A block is an area of code written in the format of:
#	block-head:
#		1st block line
#		2nd block line
#		...

# Where a block line is more Python code (even another block), and the block head is of
# the following format: block_keyword block_name(argument1,argument2,...) Block keywords
# you already know are "if", "for", and "while".

# Functions are defined using the block keyword "def", following with the function's name
# as the block's name.

def my_function():
	print("Hello From My Function!")

# Functions may also receive arguments
def my_function_with_args(username, greeting):
	print("Hello, %s, From My Function!, I wish you %s."%(username, greeting))

# Functions may return a value to the caller, using the keyword "return"
def sum_two_numbers(a, b):
	return a + b

# First, the function must be defined. Then it can be called by writing the function's name,
# placing any required arguments within the brackets.

my_function() #prints a simple greeting
my_function_with_args("John Doe", "a great year") #prints the greeting with arguments
# filling in the required variables
x = sum_two_numbers(1,2) #this assigns values for a & b in the sum function, and assigns
# x a value of 3
print(x)

# ___Exercise___
# 1. Add a function named "list_benefits()" that returns the following list of strings: 
#	"More organized code", "More readable code", "Easter code reuse", "Allowing
#	programmers to share and connect code together"
# 2. Add a function named "build_sentence(info)" which receives a single argument containing a
#	a string and returns a sentence starting with the given string and ending with the
#	string " is a benefit of functions!"
# 3. Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
def list_benefits():
	return ["More organized code", "More readable code", "Easter code reuse",
	 "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
	return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
	list_of_benefits = list_benefits()
	for benefit in list_of_benefits:
		print(build_sentence(benefit))

name_the_benefits_of_functions()
