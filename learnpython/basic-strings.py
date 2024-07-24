astring = "Hello, World!"
print("single quotes are ' '")

print(astring)
print("(See comments in script for explanation)")

print("# characters: %s" % len(astring))
print("place of 1st o: %s" % astring.index("o"))
print("# of l's: %s" % astring.count("l"))
print("slice no. 1: %s" % astring[3:7])

#If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.
print("slice no. 2, beg to 7: %s" % astring[:7])
print("slice no. 3, 3 to end: %s" % astring[3:])

#Using negative numbers maked the character count start at the end of the string.
print("slice no. 4, last character: %s" % astring[-1])

#extended slice syntax = [start:stop:step]; the following starts at the 3rd character, ends at the 7th, and skips one.
print("slice no. 5: %s" % astring[3:7:2])
print("slice no. 6: %s" % astring[2:11:2])
print("slice 3:7: %s" % astring[3:7])
print("slice 3:7:1: %s" % astring[3:7:1])
print("The last two produce the same result.")

#Python does not have a reverse string command, like strrev in C, but you can reverse a string by using the syntax to print each letter in reverse order.
print("In reverse: %s" % astring[::-1])

print("Uppercase: %s" % astring.upper())
print("Lowercase: %s" % astring.lower())
print("Does it start with 'Hello'?: %s" % astring.startswith("Hello"))
print("Does it end with 'asdfasdfasdf'?: %s" % astring.endswith("asdfasdfasdf"))
print("This splits the string at the space: %s" % astring.split(" "))
bstring = "Does this thing work?"
print("Another example: %s" % bstring.split(" "))
