#! /usr/bin/env python

# Get Programming: Learn to Code with Python, by Ana Bell
# borrowed from library 2024-07-05; renewed 2024-07-27

# Unit 6: Working with mutable objects
# Lesson 25: Working with Lists

print("QC 25.2")
desk_items = ["stapler", "tape", "keyboard", "monitor", "mouse"]
print("You have the following list:\n", desk_items)

print("print(desk_items[1]) prints 'tape': ", desk_items[1])
print("print(desk_items[4]) prints 'mouse': ", desk_items[4])
print("print(desk_items[5]) prints an error: list item out of range")
print("print(desk_items[0]) prints 'stapler': ", desk_items[0])

print("\n~~~~~~~~\n")

print("QC 25.3")

L = ["one", "three", "two", "three", "four", "three", "three", "five"]
print("Given the following list, what's printed by the following code?\n", L)

print("L.count('one') prints 1: ", L.count("one"))
print("L.count('three') prints 4: ", L.count("three"))
print("L.count('zero') prints 0: ", L.count("zero"))
print("len(L) prints 8: ", len(L))
print("L.index('two') prints 2: ", L.index("two"))
print("L.index('zero') prints ValueError: 0 is not in list")

print("\n~~~~~~~~\n")

print("QC 25.4")

one = [1]
print("List: one =>", one)
one.append("1")
print("After one.append('1') =>", one)
print("\n")
zero = []
print("List: zero =>", zero)
zero.append(0)
print("After zero.append(0) =>", zero)
zero.append(["zero"])
print("After zero.append(['zero']) =>", zero)
print("\n")
two = [1, 2]
print("List: two =>", two)
three = [7, 8]
print("List: three =>", three)
three.extend(two)
print("After three.extend(two) =>", three)
print("\n")
four = [1,2,3,4]
print("List: four =>", four)
four.insert(len(four), 5)
print("After four.insert(len(four), 5) =>", four)
four.insert(0, 0)
print("After four.insert(0, 0) =>", four)

print("\n~~~~~~~~\n")

print("QC 25.5")
pi = [3, ".", 1, 4, 1, 5, 9]
print("List: pi =>", pi)
pi.pop(1)
print("pi.pop(1) removes '.':", pi)
pi.pop()
print("pi.pop() removes last item, 9:", pi)
pi.pop()
print("pi.pop() again removes 5:", pi)

print("\n~~~~~~~~\n")

print("QC 25.6")
L = [1, 2, 3, 5, 7, 11, 13, 17]
print("List: L =>", L)
L[3] = 4
print("'L[3] = 4' replaces the 5 with 4:", L)
L[4] = 6
print("'L[4] = 6' replaces the 7 with 6:", L)
L[-1] = L[0]
print("'L[-1] = L[0]' replaces the 17 with 1:", L)
L[0] = L[1] + 1
print("'L[0] = L[1] + 1' replaces the 1st 1 with 3:", L)

print("\n~~~~~~~~\n")

print("Points to Remember")
print(" ~ Lists can be empty or can contain elements.")
print(" ~ You can add an element to the end of a list, at a specific index, or you can extend it by more than one element.")
print(" ~ You can remove elements from the list, from the end or from a specific index.")
print(" ~ You can change element values.")
print(" ~ Every action mutates the list, so the list object changes without you having to reassign it to another variable.")

print("\n~~~~~~~~\n")

print("Q25.1")
menu = []
print("List: menu =>", menu)
menu.append("pizza")
menu.append("beer")
menu.append("fries")
menu.append("wings")
menu.append("salad")
print("Step 1 =>", menu)
menu.pop(1)
menu[0] = menu[-1]
menu[-1] = "pizza"
print("Step 2 =>", menu)
menu[1] = "quinoa"
menu[2] = "steak"
menu.pop(-1)
print("Step 3 =>", menu)

print("\n~~~~~~~~\n")

print("Q25.2")
# Write a function named unique. It takes in one parameter, a list named L.
# The function doesn't mutate L and returns a new list containing only the unique elements in L.

def unique(L):
    L_unique = [] # initiates list L
    for n in L:
        if n not in L_unique: # if item n is not in the list
            L_unique.append(n) # add it to the list
    return L_unique

print("Q25.3")
# Write a function named common. It takes in two parameters, lists named L1 and L2.
# The function doesn't mutate L1 or L2. It returns True if every unique element in L1
# is in L2 and if every unique element in L2 is in L1. It returns False otherwise.
# Hint: try to reuse your function from Q25.2.

def common(L1, L2):
    """
    L1, list of elements
    L2, another list of elements
    """
    unique_L1 = unique(L1) # calls the unique function for list 1
    unique_L2 = unique(L2) # calls the unique function for list 2
    length_L1 = len(unique_L1)
    length_L2 = len(unique_L2)
    if length_L1 != length_L2: #checks lengths of list because they should match
        return False
    else:
        for i in range(length_L1):
            if L1[i] not in L2:
                return False
        return True

print("L1: [1,2,3], L2: [3,2,1] =>", common([1,2,3], [3,1,2]))
print("L1: [1,1,1], L2: [1] =>", common([1,1,1], [1]))
print("L1: [1], L2: [1,2] =>", common([1], [1,2]))

L1 = []
L2 = []
print("Enter numbers from 1-9")
a = int(input("Enter a number for the list: "))
L1.append(a)
b = int(input("Enter another number: "))
L2.append(b)
c = int(input("And another number: "))
L1.append(c)
d = int(input("Again...: "))
L2.append(d)
e = int(input("Go on, do it again: "))
L1.append(e)
f = int(input("Last time, I swear: "))
L2.append(f)

print(L1)
print(L2)
if common(L1, L2) == True:
    print("Yay! They match!")
else:
    print("Darn, they don't match.")

