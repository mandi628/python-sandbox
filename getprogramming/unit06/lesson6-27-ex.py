#! /usr/bin/env python

# Get Programming: Learn to Code with Python, by Ana Belle

# Unit 6: Working with mutable data types
# Lesson 27: Dictionaries as maps between objects

print("Q 27.1")
# Write a program that uses dictionaries to accomplish the following task.
# Given a dictionary of song names (strings) mapped to ratings(integers),
# print the song names of all songs that are rated exactly 5.

songs = {}

songs["Singin' in the Rain"] = 4
songs["Twinkle, Twinkle"] = 3
songs["Humpty Dumpty"] = 5
songs["Jump"] = 5

for s in songs.keys():
    if songs[s] == 5:
        print(s)

print(songs)

# I don't know where I'm stuck, but I couldn't do these exercises without the answer key.

print("\n~~~~~~~~\n")

print("Q 27.2")

#Write a function name replace. It takes in one dictionary, d, and two values, v and e. 
# The function doesn't return anything. It mutates d such that all the values v in d
# are replaced with e. For example:
#    replace({1:2, 3:4, 4:2}, 2, 7) mutates d to {1:7, 3:4, 4:7}
#    replace({1:2, 3:1, 4:2}, 1, 2) mutates d to {1:2, 3:2, 4:2}

def replace(d, v, e):
    for k in d:
        if d[k] == v:
            d[k] = e

da = {1:2, 3:4, 4:2}
print(da)
dar = replace(da, 2, 7)
print(dar)

d2 = {1:2, 3:1, 4:2}
print(d2)
print("Replace 1 with 2:")
print(replace(d2,1,2))

# Well, for this one, I copied from the answer key, and it's not working. I don't know
# if I'm not calling the function right or something is wrong with the function, but I'm
# getting a result of "None".

print("\n~~~~~~~~\n")

print("Q 27.3")

# Write a function named invert. It takes in one dictionary, d. The function returns a new
# dictionary, d_inv. The keys in d_inv are the unique values in d. The value corresponding
# to a key in d_inv is a list. The list contains all the keys in d that mapped to the same
# value in d. For example:
#     invert({1:2, 3:4, 5:6}) returns {2: [1], 4: [3], 6: [5]}
#     invert({1:2, 2:1, 3:3}) returns {1: [2], 2: [1], 3: [3]}
#     invert({1:1, 3:1, 5:1}) returns {1: [1, 3, 5]}

def invert(d):
    d_inv = {}
    for k in d:
        v = d[k]
        if v not in d_inv:
            d_inv[v] = [k]
        else:
            d_inv[v].append(k)
    return d_inv

d = {1:2, 3:4, 5:6}
print(d)
d_inv = invert(d)
print(d_inv)

g = {1:2, 2:1, 3:3}
print(g)
g_inv = invert(g)
print(g_inv)

p = {1:1, 3:1, 5:1}
print(p)
p_inv = invert(p)
print(p_inv)
