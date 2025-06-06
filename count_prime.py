#count digits that are prime numbers
num = int(input("Enter a number: "))
count = 0
temp = abs(num)

def is_prime(d):
    return d in [2, 3, 5, 7]

while temp > 0:
    digit = temp % 10
    if is_prime(digit):
        count += 1
    temp //= 10

print("Count of prime digits:", count)
