#! /usr/bin/env python

def read_file(file):
    """
    file, a file object
    Starting from the first line, it reads every 2 lines
    and stores them in a tuple.
    Starting from the second line, it reads every 2 lines
    and stores them in a tuple.
    Returns a tuple of the two tuples.
    """
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n", "")
        if line_count % 2 == 0:
            first_every_2 += (stripped_line,)
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line,)
        line_count += 1
    return (first_every_2, second_every_2)

def sanitize(some_tuple):
    """
    phones, a tuple of strings
    Removes all spaces, dashes, and open/closed parentheses
    in each string
    Returns a tuple with cleaned up string elements
    """
    clean_string = ()
    for st in some_tuple:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        clean_string += (st,)
    return clean_string

def analyze_friends(names, phones, all_areacodes, all_places):
    """
    names, a tuple of friend names
    phones, a tuple of phone numbers without special symbols
    all_areacodes, a tuple of strings for the area codes
    all_places, a tuple of strings for the US states
    Prints out how many friends you have and every unique
    state that is represented by their phone numbers
    """
    def get_unique_area_codes():
        """
        Returns a tuple of all unique area codes in phones
        """
        area_codes = () # Initialize the tuple
        for ph in phones:
            if ph[0:3] not in area_codes: # Checks first 3 characters in phone string
                area_codes += (ph[0:3],) # Adds it to the tuple if it's not already there
        return area_codes

    def get_states(some_areacodes):
        """
        some_areacodes, a tuple of area codes
        Returns a tuple of the states associated with those area codes
        """
        states = () # Initialize the tuple
        for ac in some_areacodes:
            if ac not in all_areacodes: # If the area code is not in the list, it gives a response
                states += ("BAD AREACODE",)
            else:
                index = all_areacodes.index(ac) # Gives the index position of the area code
                states += (all_places[index],) # Uses the index position to lookup the state
        return states

    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)

    print("You have", num_friends, "friends!")
    print("They live in", unique_states)

friends_file = open('friends.txt')
(names, phones) = read_file(friends_file)
areacodes_file = open('map_areacodes_states.txt')
(areacodes, states) = read_file(areacodes_file)

clean_phones = sanitize(phones)

analyze_friends(names, clean_phones, areacodes, states)

friends_file.close()
areacodes_file.close()
