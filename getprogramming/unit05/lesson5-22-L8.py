#!/usr/bin/env python

print("Listing 22.8 - Sandwich Function")

def sandwich(kind_of_sandwich):
    print("------------")
    print(kind_of_sandwich())
    print("------------")

def blt():
    my_blt = " bacon\nlettuce\n tomato"
    return my_blt

def breakfast():
    my_ec = " eggegg\n cheese"
    return my_ec

def veg():
    my_veg = "lettuce\n tomato\n cheese \npickles"
    return my_veg

print(sandwich(blt))
print(sandwich(breakfast))
print(sandwich(veg))
