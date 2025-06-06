#denomination of four digit number
num = int(input("Enter a 4-digit number: "))

if 1000 <= num <= 9999:
    thousands = num // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    ones = num % 10

    print(f"{thousands}*1000 = {thousands*1000}")
    print(f"{hundreds}*100 = {hundreds*100}")
    print(f"{tens}*10 = {tens*10}")
    print(f"{ones}*1 = {ones}")
else:
    print("Please enter a 4-digit number.")
