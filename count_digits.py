#count number of digits
num = int(input("Enter a number: "))
count = 0
temp = abs(num)

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits:", count)
