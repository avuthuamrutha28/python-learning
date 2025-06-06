#sum the digits repeatedly until it becomes single digit
num = int(input("Enter a number: "))

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

while num >= 10:
    num = digit_sum(num)

print("Single digit sum:", num)
