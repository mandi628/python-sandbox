#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 6: While Loop

print("Challenge 048")

# Ask for the name of somebody the user want to invite to a party.
# After this, display the message "[name] has now been invited"
# and add 1 to the count. Then ask if they want to invite somebody
# else. Keep repeating this until they no longer want to invite
# anyone else to the party and then display how many people they
# have coming to the party.

guests = 0
guest_list = [] # Extra
again = "y"
while again == "y":
    name = input("Who do you want to invite to the party? ")
    guest_list.append(name) # Extra
    print(name, "has now been invited.")
    guests += 1
    again = input("Do you want to invite another? (y/n) ")
print("You have invited %d guests to the party." % guests)
print("Your guests are: ", guest_list) # Extra
