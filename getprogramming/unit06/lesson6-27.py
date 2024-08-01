#! /usr/bin/env python

# Get Programming: Learn to Code with Python, Ana Bell
# borrowed from library 2024-07-05; renewed 2024-07-27

# Unit 6: Working with mutable objects
# Lesson 27: Dictionaries as maps between objects

print("QC 27.1")
# Write a line of code that creates a dictionary and binds it to a variable with an appropriate
# name. Also indicate the keys and values.

print("1) Empty dictionary fo employee names and their phone numbers and addresses.")
print("    employees = {}\n    key: string of employee name\n    values: tuple of string phone number and string address")
print("\n")
print("2) Empty dictionary of cities and the number of inches of snow each city got in 1990 and 2000.")
print("    city_snow = {}\n    key: string of city name\n    values: tuple of strings, 1990, snow, 2000, snow")
print("\n")
print("3) Dictionary of items in a house and their value: a TV worth $2,000 and a sofa worth $1,500.")
print("    valuables = {'TV': 2000, 'sofa': 1500}\n    key: item name\n    value: int value")

print("\n~~~~~~~~\n")

print("QC 27.2")
# For each of the following, how many entries are in the dictionary? What the type of the keys
# and what's the type of the values?

print("1) d = {1:-1, 2:-2, 3:-3}\n    3 entries; key = int; values = int")
d1 = {1:-1, 2:-2, 3:-3}
print(d1)
print("2) d = {'1':1, '2':2, '3':3}\n    3 entries; key = string; values = int")
d2 = {'1':1, '2':2, '3':3}
print(d2)
print("3) d = {2:[0,2], 5:[1,1,1,1,1], 3:[2,1,0]}\n    3 entries; key = int; values = lists of int")
d3 = {2:[0,2], 5:[1,1,1,1,1], 3:[2,1,0]}
print(d3)

print("\n~~~~~~~~\n")

print("Listing 27.1")
legs = {}
print("Initiate dictionary 'legs':", legs)
legs["human"] = 2
print("Add legs['human'] = 2:", legs)
legs["cat"] = 4
print("Add legs['cat'] = 4:", legs)
legs["snake"] = 0
print("Add legs['snake'] = 0:", legs)
print("len(legs) gives the number of entries:", len(legs))
legs["cat"] = 3
print("Change value for legs['cat'] = 3:", legs)
print("len(legs) shows same number:", len(legs))
print(legs)

print("\n~~~~~~~~\n")

print("QC 27.3")
city_pop = {}
print("Initiate city_pop = {}:", city_pop)
city_pop["LA"] = 3884
print("Add LA:", city_pop)
city_pop["NYC"] = 8406
print("Add NYC:", city_pop)
city_pop["SF"] = 837
print("Add SF:", city_pop)
city_pop["LA"] = 4031
print("Edit LA:", city_pop)

print("\n~~~~~~~~\n")

print("Listing 27.2")
household = {"person":4, "cat":2, "dog":1, "fish":2}
print("Initiate dictionary:", household)
removed = household.pop("fish")
print("Removed with pop() function:", removed)
print("Remaining dictionary:", household)
print("--------")
print("QC 27.4")
constants = {"pi":3.14, "e":2.72, "pyth":1.41, "golden":1.62}
print("Initiate dictionary:", constants)
print("Remove pi:", constants.pop("pi"), "\n", constants)
print("Remove pyth:", constants.pop("pyth"), "\n", constants)
print("Remove i: Key error 'i'")
print(constants)
