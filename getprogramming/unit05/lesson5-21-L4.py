# Get Programming: Learn to Code with Python, by Ana Bell

# Unit 5: Organizing Your Code Into Reuseable Blocks
# Lesson 21: Achieveing modularity and abstraction with fuctions

print("Listing 21.4 - Returning a tuple")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def add_sub(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    return (add, sub)

(a, b) = add_sub(num1, num2)
print(a, b)
