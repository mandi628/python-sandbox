# Get Programming: Learn to Code with Python, by Ana Bell
# Checked out from library on 2024.07.06

# Unit 2: Strings, Tuples, and Interacting with the User
# Lesson 8: Advanced string operations

print("Quick check 8.1")
a = "python 4 ever&EVER"
print("a.find('E') = 14: %s" % a.find("E"))
print("a.find('eve') = 9: %s" % a.find("eve"))
print("a.find('rev') = -1: %s" % a.find("rev"))
print("a.find('VER') = 15: %s" % a.find("VER"))
print("a.find(' ') = 6: %s" % a.find(' '))
print("a.rfind(' ') = 8: %s" % a.rfind(' '))

print("\n~~~~~~~~\n")

print("Quick check 8.2")
print("'on' in a = TRUE:")
print("on" in a)
print("'' in a = TRUE:")
print("" in a)
print("'2 * 2' in a = FALSE:")
print("2 * 2" in a)

print("\n~~~~~~~~\n")

print("Quick check 8.3")
print("a.count('ev') = 1: %s" % a.count("ev"))
print("a.count(' ') = 2: %s" % a.count(" "))
print("a.count(' 4 ') = 1: %s" % a.count(" 4 "))
print("a.count('eVer') = 0: %s" % a.count("eVer"))

print("\n~~~~~~~~\n")

print("Quick check 8.4")
b = "Raining in the spring time."
print(b)
ba = b.replace("R", "r")
print(ba)
bb = b.replace("ing", "")
print(bb)
bc = b.replace("!", ".")
print(bc)
bd = b.replace("time", "tiempo")
print(bd)

print("\n~~~~~~~~\n")

print("Quick check 8.5")
print("La" + "la" + "Land")
print("USA" + " vs " + "Canada")
b = "NYC "
c = 5
print(b * c)
color = "red"
shape = "circle "
number = 3
print(number * (color + "-" + shape))

print("\n~~~~~~~~\n")

print("Q8.1")
s = "Eat Work Play Sleep repeat"
print(s)
w = "work"
p = "play"
z = "ing"
print(w + z + " " + p + z)
