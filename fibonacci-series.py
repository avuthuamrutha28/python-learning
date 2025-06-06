#to print fibonacci series upto a number
a, b = 0, 1
print("Fibonacci series up to 34:")
while a <= 34:
    print(a, end=" ")
    a, b = b, a + b
