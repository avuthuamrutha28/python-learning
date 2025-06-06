#reverse the number given by user
num = int(input("Enter a number: "))
reverse = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse of the number:", reverse)

