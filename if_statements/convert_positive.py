#Write a program to accept a number from the user. If the number is negative then convert it to a positive number and print; if it is a positive number, print it as is.
number=int(input("Enter a number:"))

if number<0:
    positive_number=-1*number
    print(f"The positive number is {positive_number}")
else:
    print(f"The number is {number}")
