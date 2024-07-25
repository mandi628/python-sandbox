#! /usr/bin/env python

def read_file(file):
    """
    file, a file object
    Starting from the first line, it read every 2 lines
    and stores them in a tuple.
    Starting from the second line, it reads every 2 lines
    and stores them in a tuple.
    Returns a tuple of the two tuples.
    """
    first_every_2 = () # initializes the tuple for the names
    second_every_2 = () # initializes the tuple for the phone numbers
    line_count = 0 # Counter for the line number
    for line in file:
        stripped_line = line.replace("\n", "") # Removes newline character
        if line_count % 2 == 0: # Odd-numbered lines (but I think this is even numbered lines)
            first_every_2 += (stripped_line,) # Adds line to name tuple
        elif line_count % 2 == 1: # Even-numbered lines
            second_every_2 += (stripped_line,) # Adds line to number tuple
        line_count += 1 # increases the line count
    return (first_every_2, second_every_2) # calls the tuples in a tupple, together

def sanitize(some_tuple):
    """
    phones, a tuple of strings
    Removes all spaces, dashes, and open/closed parentheses
    in each string
    Returns a tuple with cleaned up string elements
    """
    # This function will standardize the phone number format
    clean_string = () # Initializes the clean phone number tuple
    for st in some_tuple:
        st = st.replace(" ", "") # Removes spaces from string
        st = st.replace("-", "") # Removes dashes from string
        st = st.replace("(", "") # Removes open paren from string
        st = st.replace(")", "") # Removes closed paren from string
        clean_string += (st,) # Adds string to new tuple
    return clean_string

friends_file = open('friends.txt') # Opens the text file
(names, phones) = read_file(friends_file) # Calls the read-file function above

print(names) # Prints the names tuple
print(phones) # Prints the phones tuple
clean_phones = sanitize(phones) # Calls the sanitize function on the phones tuple

print(clean_phones) # Prints the new standardized phone number tuple
friends_file.close() # Closes the text file
