def f(a, b):
    x = a + b
    y = a - b
    print("Inside the function: ", x * y)
    return x / y

a = 1
b = 2
x = 5
y = 6

print("    Return from function: ", f(x, y))
print("    Return from function: ", f(a, b))
print("    Return from function: ", f(x, a))
print("    Return from function: ", f(y, b))
