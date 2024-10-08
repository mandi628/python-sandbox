s = "Strings are awesome!"
# Lenth should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

#Slice the string into bits
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
	print("String starts with 'Str'. Good!")

# Check how string ends
if s.endswith("ome!"):
	print("String ends with 'ome!'. Good!")

#Split the string into three separate strings, each containing only a word.
print("Split the words of the string: %s" % s.split(" "))
