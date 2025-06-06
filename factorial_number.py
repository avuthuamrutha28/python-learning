# factorial of a number
number = int(input("Enter a number:"))
factorial = 1
if number < 0:
    print("factorial can not be negative")
elif number == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
print(f"The factorial of {number} is {factorial}")
