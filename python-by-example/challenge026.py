#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

print("Challenge 026")
# Pig Latin takes the first consonant of a word, moves it to the end of the word
# and adds on an "ay". If a word begins with a vowel you just add "way" to the
# end. For example, pig becomes igpay, banana becomes ananabay, and aadvark
# becomes aadvarkway. Create a program that will ask the user to enter a word and
# change it into Pig Latin. Make sure the new words is displayed in lower case.
word = input("Enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]

if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword)
