#print odd number series upto n and sum
n = int(input("Enter a number: "))
total = 0

print("Odd number series:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
    total += i

print(f"\nSum of odd numbers up to {n} = {total}")
