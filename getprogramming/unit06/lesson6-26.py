#! /usr/bin/env python

# Get Programming: Learn to Code with Python, by Ana Bell
# borrowed from library 2024-07-05; renewed 2024-07-27

# Unit 6: Working with mutable objects
# Lesson 26: Advanced operations with lists

print("QC 26.1")
print("Let's start with a word: programming")
L = ["p", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g"]
print("List: L =>", L)
L.reverse()
print("After L.reverse() =>", L)
L.sort()
print("After L.sort() =>", L)
L.reverse()
print("After L.reverse() again =>", L)
L.reverse()
print("After another L.reverse() =>", L)
L.sort()
print("After another L.sort() =>", L)

print("\n~~~~~~~~\n")

print("Listing 26.2")
L = [[], [], []] # An empty list of 3 lists
print("List: L =>", L)
L[0] = [1,2,3] # Sets index point 0 with the list of [1, 2, 3]
print("L[0] = [1,2,3] =>", L)
L[1].append('t') # Adds 't' to the index 1 list
print("L[1].append('t') =>", L)
L[1].append('o') # Adds 'o' to the index 1 list, which now will have 2 elements
print("L[1].append('o') =>", L)
L[1][0] = 'd' # Changes the index 0 element of the index 1 list from d to t
print("L[1][0] = 'd' =>", L)
L[2].append('g')
L[2].append('o')
L[2].append('o')
L[2].append('d')
print("My own addition =>", L)
L.append("dear")
print("Another addition =>", L)

print("\n~~~~~~~~\n")

print("Listing 26.3 & QC 26.2")
print("\nUse lists inside of lists to display a tic-tac-toe board.")

x = 'x'
o = 'o'
empty = '_'

board = [[x, empty, o], [empty, x, o], [x, empty, empty]]
print(board)

board1 = [[empty, empty, empty], [x, x, x], [o, o, o]]
print(board1)

board2 = [[x, o, x, o], [o, o, x, x], [o, empty, x, x]]
print(board2)

print("\n~~~~~~~~\n")

print("QC 26.3")
print("\nSplit strings by an element.")
emails = "zebra@zoo.com,red@colors.com,tom.sawyer@book.com,pea@veg.com"
print("This is a string of emails:", emails)
emails_list = emails.split(',')
print("Using emails.split(',') we now have a list: =>", emails_list)
abc = " abcdefghijklmnopqrstuvwxyz"
print("Now an alpha string:", abc)
abc_list = abc.split(' ')
print("abc.split(' ') gives us =>", abc_list)
spaces = "spaces and more spaces"
print("Spaces string:", spaces)
space_list = spaces.split(' ')
print("Now split into words =>", space_list)
HG = "the secret of life is 42"
print("Hitchhiker's Guide string:", HG)
HG_list = HG.split('s')
print("Split on the letter 's' =>", HG_list)

print("\n~~~~~~~~\n")

print("Listing 26.4 - Stacks")
print("\nDemonstrates first-in-last-out structure")
stack = []
cook = ['blueberry', 'blueberry', 'blueberry']
print("Cook 3 blueberry pancakes:", cook)
stack.extend(cook)
print("Add them to the plate (extend):", stack)
stack.pop()
print("Someone eats one (pop):", stack)
stack.pop()
print("Another one eaten:", stack)
cook = ['chocolate', 'chocolate']
print("Cooking 2 chocolate pancakes:", cook)
stack.extend(cook)
print("Add them to the plate:", stack)
stack.pop()
print("One more eaten:", stack)
cook = ['blueberry', 'blueberry']
print("Two more blueberry this time:", cook)
stack.extend(cook)
print("Add them to the stack...", stack)
stack.pop()
print("Eating another one:", stack)
stack.pop()
print("And another...", stack)
stack.pop()
print("And last one, leaves one left over:", stack)

print("\n~~~~~~~~\n")

print("Listing 26.5 - Queues")
print("\nDemonstrates the first-in-first-out structure")
line = []
print("Line at the grocery store:", line)
line.append('Ana')
print("Ana joins the line (append):", line)
line.append('Bob')
print("Bob joins the line:", line)
line.pop(0)
print("Ana is served (pop):", line)
line.append('Claire')
print("Claire joins the line:", line)
line.append('Dave')
print("Dave joins the line:", line)
line.pop(0)
print("Bob is served:", line)
line.pop(0)
print("Claire is served:", line)
line.pop(0)
print("Dave is served:", line)

print("\n~~~~~~~~\n")

print("Q26.1")
# Write a program that takes in a string containing city names separated by commas, and then
# prints a list of the city names in sorted order.
print("\nTask 1: From a string, print a list of cities, sorted...")
cities = "San Francisco, Boston, Chicago, Indianapolis"
cities_list = cities.split(", ")
cities_list.sort()
print(cities_list)
print("--------")
# Write a function named is_permutation. It takes in two lists, L1 and L2.
# The function return True if L1 and L2 are permutations of each other.
# It returns False otherwise. Every element in L1 is in L2, and vice versa, only
# arranged in a different order.
print("Task 2: Permutations")

def is_permutations(L1, L2):
    """
    L1, a list
    L2, another list
    Sorts and compares the lists
    If they are the same, return True
    If the are different, return False
    """
    L1.sort()
    L2.sort()
    return L1 == L2

print("For L1[1,2,3] and L2[3,1,2]:", is_permutations([1,2,3],[3,1,2]))
print("For L1[1,1,1,2] and L2[1,2,1,1]:", is_permutations([1,1,1,2], [1,2,1,1]))
print("For L1[1,2,3,1] and L2[1,2,3]:", is_permutations([1,2,3,1], [1,2,3]))
