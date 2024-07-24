# Get Programming: Learn to Code with Python, by Ana Bell

# Unit 5: Organizing Your Code Into Reuseable Blocks
# Lesson 21: Achieveing modularity and abstraction with fuctions

print("Quick Check 21.7")
print("Let's make a silly sentence.\n")
# Given the following fuction and variable initializations, what will each line
# print, if executed in the following order:

def make_sentence(who, what):
    """
    who, string - from input
    what, string - from input
    Concatenates who and what with "is"
    Returns sentence string
    """
    doing = who + " is " + what
    return doing

def show_story(person, action, number, thing):
    """
    person, string (from make_sentence(who))
    action, string(from make_sentence(what))
    number, string - from input
    thing, string - from input
    Runs make_sentence() for variable "what"
    Creates a phrase combining number and thing
    Creates sentence string from previous two actions
    Prints story
    """
    what = make_sentence(person, action)
    num_times = str(number) + " " + thing
    my_story = what + " " + num_times
    print(my_story)

#who = "Hector"
who = input("Enter a name: ")
#what = "eating"
what = input("Enter an action that ends with 'ing': ")
#thing = "bananas"
thing = input("Enter an object: ")
#number = 8
number = input("Enter a number: ")

# Test lines
#sentence = make_sentence(who, thing) # nothing printed
#print(make_sentence(who, what)) # "Hector is eating" printed
#your_story = show_story(who, what, number, thing) # "Hector is eating 8 bananas"
#my_story = show_story(sentence, what, number, thing) # "Hector is bananas is eating 8 bananas"
#print(your_story) # None, because "your_story" isn't defined
your_story = show_story(who, what, number, thing)

# Don't need another print function here, because the last line of the "show_story"
# function is a call to print it.
