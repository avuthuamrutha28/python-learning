#prime numbers between two numbers
low = int(input("Enter the first number: "))
high = int(input("Enter the second number: "))

print(f"Prime numbers between {low} and {high} are:")
for num in range(min(low, high), max(low, high) + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
