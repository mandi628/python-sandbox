#! /usr/bin/env python3

filename = input("Enter the filename you'd like to decode: ")
#file = open("messages/message_file1.txt")
file = open(filename)
message_file = file

msg = {'6': 'computers', '3': 'love', '1': 'I', '4': 'dogs', '5': 'you', '2': 'cats', '7': 'meet', '8': 'elephants', '9': 'parade', '0': 'party', 's': 'Suzi', 't': 'Tess', 'm': 'Micky', 'h': 'Ashleigh', 'a': 'Abbie', 'c': 'Mama', 'x': 'at', 'b': 'this', 'z': 'is', 'd': 'really', 'e': 'cool',
}

def decode(message_file):
    cypher = str(file.read())
    print(cypher)
    char = ()
    start = 0
    end = 0
    for char in cypher:
        if char == "\n":
            char = char + (cypher[start:end])
            start = end + 1
            end = end + 1
        else:
            end = end + 1
    print(char)

msg = decode(message_file)
file.close()
