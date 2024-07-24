# Get Programming: Learn to Code with Python, by Ana Bell

# Unit 5: Organizing Your Code Into Reuseable Blocks
# Lesson 21: Achieveing modularity and abstraction with fuctions

print("Listing 21.3 - How to make a call to a function")

def word_length(word1, word2):
    word = word1 + word2
    return len(word)
    print("this never gets printed")

length1 = word_length("Rob", "Banks")
length2 = word_length("Barbie", "Ken")
length3 = word_length("Holly", "Jolly")

print("One name is", length1, "letters long.")
print("Another name is", length2, "letters long.")
print("The final name is", length3, "letters long.")

print("\n~~~~~~~~\n")

def name_length(first, middle, last):
    name = first + middle + last
    return len(name)

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")

fullName = name_length(first, middle, last)
print("Your full name is", fullName, "letters long.")

print("\n~~~~~~~~\n")

