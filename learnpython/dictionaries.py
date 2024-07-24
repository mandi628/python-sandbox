# A dictionary is a data type similar to arrays, but works with keys and values
# instaed of indexes. Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.) instead of using its
# index to address it.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Another way of initalizing the same thing:
phonebook = {
	"John" : 938477566,
	"Jack" : 938377264,
	"Jill" : 947662781
}
print(phonebook)

# Dictionaries can be interated over, just like a list. However, a dictionary, unlike a list,
# does not keep the order of the values stored in it. To iterate over key value pairs, use
# the following syntax:
for name, number in phonebook.items():
	print("Phone number of %s is %d" % (name, number))

# To remove a specified index from a dictionary, use either of the following:
del phonebook["John"]
print(phonebook)

phonebook["Anne"] = 847987887
print(phonebook)

phonebook.pop("Anne")
print(phonebook)

phonebook["John"] = 938477566
print(phonebook)

# __Exercise__
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the 
# phonebook.
phonebook["Jake"] = 938273443
print(phonebook)

del phonebook["Jill"]
print(phonebook)

#testing code
if "Jake" in phonebook:
	print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
	print("Jill is not listed in the phonebook.")



