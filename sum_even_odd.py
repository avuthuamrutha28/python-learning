# sum of even and odd numbers upto selected number
number = int(input("Enter a number:"))

sum_even = 0
sum_odd = 0
for i in range(0, number+1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of even numbers are:{sum_even}")
print(f"The sum of odd numbers are:{sum_odd}")
