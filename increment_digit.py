#increment each digit by one in five digit number
num = input("Enter a 5-digit number: ")

if len(num) == 5 and num.isdigit():
    result = ''
    for digit in num:
        new_digit = (int(digit) + 1) % 10
        result += str(new_digit)
    print("Output:", result)
else:
    print("Please enter a valid 5-digit number.")
