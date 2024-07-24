x = 2
print(x == 2) #prints out True
print(x == 3) #prints out False
print(x < 3) #prints out True

# Note that variable assignment is done using a single equals operator "="
# whereas comparison between two variables is done using the double equals operator "=="
# The "not equals" operator is marked as "!="

# The "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23
if name == "John" and age == 23:
	print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
	print("Your name is either John or Rick.")

# The "in" operator could be used to check if a specified object exists within
# an iterable object container, such as a list
name = "John"
if name in ["John", "Rick"]:
	print("Your name is either John or Rick.")

# Python uses indentation to define code blocks, instead of barckets.
# The standard Python indentation is 4 spaces, but tabs and any other space size will work,
# as long as it's consistent. Notice that code blocks do not need any termination.

statement = False
another_statement = True
if statement is True:
 pass
elif another_statement is True:
 pass
else:
 pass

x = 2
if x == 2:
 print("x equals two!")
else:
 print("x does not equal two.")

x = 3
if x == 7:
 print("You guessed my number!")
else:
 print("Oops! Try again!")

# A statement is evaluated as true if one of the following is correct:
# 1. The "True" boolean variable is given, or calculated using an expression
# 2. An object which is not considered "empty" is passed.
# Examples for ebjects considered as empty:
# 1. An empty string, ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

# Unlike the double equals operator "==", the "is" operator does not match the values
# of the variables, but the isntances themselves.
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# Using "not" before a boolean expression inverts it
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
