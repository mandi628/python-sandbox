#! /usr/bin/env python3

file = open('friends.txt', 'a')

name = input("What is your friend's name? ")
phone = input("What is your friend's phone number? ")

file.write(name + "\n")
file.write(phone + "\n")
file.close()
