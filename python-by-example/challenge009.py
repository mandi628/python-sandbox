#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 009")
# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
days = int(input("Enter a number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In", days, "days, there are:")
print(hours, "hours")
print(minutes, "minutes")
print("and", seconds, "seconds")
