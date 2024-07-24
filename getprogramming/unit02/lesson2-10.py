# Get Programming: Learning to Code in Python, by Ana Bell
# Borrowed from library on 2024.07.06

# Unit 2: Strings, Tuples, and Interacting with the User
# Lesson 10: Tuple objects: sequences of any kind of object

print("Quick check 10.2")
print("len(('hi', 'hello', 'hey', 'hi')) = 4: %s" % len(("hi", "hello", "hey", "hi")))
print("len(('abc', (1, 2, 3))) = 2: %s" % len(("abc", (1, 2, 3))))
print("len(((1,2),)) = 1: %s" % len(((1,2),)))
print("len(()) = 0: %s" % len(()))

print("\n~~~~~~~~\n")

print("Quick check 10.3")
print("[1] of ('abc', (1, 2, 3)) = (1, 2, 3)")
b = ("abc", (1, 2, 3))[1]
print(b)
print("[1][2] of ('abc', (1, 2, '3')) = 3")
c =  ('abc', (1, 2, '3'))[1][2]
print(c)
print("[1:3] of ('abc', (1, 2), '3', 4, ('5', '6')) = ((1, 2), '3')")
d = ('abc', (1, 2), '3', 4, ('5', '6'))[1:3]
print(d)
a = 0
t = (True, 'True')
print("If a = 0 and t = (True, 'True'), then t[a] = True")
e = t[a]
print(e)

print("\n~~~~~~~~\n")

print("Quick check 10.4")
print("len('abc') * ('no',) = ('no', 'no', 'no')")
f = len('abc') * ('no',)
print(f)
print("2 * ('no', 'no', 'no') = ('no', 'no', 'no', 'no', 'no', 'no')")
g = 2 * ('no', 'no', 'no')
print(g)
print("(0, 0, 0) + (1,) = (0, 0, 0, 1)")
h = (0, 0, 0) + (1,)
print(h)
print("(1, 1) + (1, 1) = (1, 1, 1, 1)")
i = (1, 1) + (1, 1)
print(i)

print("\n~~~~~~~~\n")

print("Quick check 10.5")
long = "hello"
short = "hi"
print("long = " + long + ", and short = " + short)
(short, long) = (long, short)
print("Now, long = " + long + ", and short = " + short)
print("--------")
s = "strong"
w = "weak"
print("s = " + s + ", and w = " + w)
(w, s) = (s, w)
print("now, s = " + s + ", and w = " + w)
print("--------")
yes = "affirmative"
no = "negative"
print("yes = " + yes + ", and no = " + no)
(yes, no) = (no, yes)
print("now, yes = " + yes + ", and no = " + no)
print("--------")

# Q10.1 Write a program that initializes the string word = "echo",
# the empty tuple t = (), and the integer count = 3. Then, write a
# sequence of commands by using the commands you learned in this lesson
# to make t = ("echo", "echo", "echo" "cho", "cho", "cho", "ho", "ho",
# "ho", "o", "o", "o") and print it. The original word is added to the
# end of the tuple, and then the original word without the first letter
# is added to the tuple, and so on. Each substring of the original word
# gets repeated count number of times.

word = "echo"
t = ()
count = 3

echo = (word,)
echo *= count
cho = (word[1:],)
cho *= count
ho = (word[2:],)
ho *= count
o = (word[-1],)
o *= count
t = echo, cho, ho, o
print(t)
