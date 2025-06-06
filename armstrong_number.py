#print armstrong number
num = int(input("Enter a number: "))
temp = num
sum_cubes = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_cubes += digit ** digits
    temp //= 10

if sum_cubes == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
