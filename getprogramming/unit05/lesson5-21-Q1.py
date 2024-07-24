# Get Programming: Learn to Code with Python, by Ana Bell

# Unit 5: Organizing Your Code Into Reuseable Blocks
# Lesson 21: Achieveing modularity and abstraction with fuctions

print("Q21.1")
print("Tip calculator")
# 1) Write a function named "calculate_total" that takes in two parameters:
#    a float named price, and an integer named percent. The function calculates
#    and returns a new number representing the price plus the tip: total = 
#    price + percent*price.

def calculate_total(price, percent):
    """
    price, float
    percent, int
    Calculate price plus tip (percentage of price)
    Return total, float
    """
    total = price + ((percent/100) * price)
    return total

# 2) Make a function call to your function with a price of 20 and a percent of 15
print("With a price of 20 and a tip of 15 percent, the total is", calculate_total(20, 15))

# 3) Complete the following code in a program to use your function.
my_price = 78.55
my_tip = 20

my_total = calculate_total(my_price, my_tip)
print("With a price of", my_price, "and a tip of", my_tip, "percent, the total is", round(my_total, 2))

your_price = float(input("\nEnter your price: "))
your_tip = int(input("Enter your tip percent (whole number): "))
your_total = calculate_total(your_price, your_tip)
print("\nWith a price of", your_price, "and a tip of", your_tip, "percent, the total is", round(your_total, 2), ".")
