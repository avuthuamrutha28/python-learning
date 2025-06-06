#Write a program to accept two numbers from the user and find the bigger of the two.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1>num2:
    print("num1 is bigger")
elif num2>num1:
    print("num2 is bigger")
else:
    print("Both are equal")