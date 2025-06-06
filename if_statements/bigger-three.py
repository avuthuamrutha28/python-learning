#Write a program to accept three numbers and find the biggest number.
a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number:"))
c=int(input("Enter a 3rd number:"))
if a>b>c:
    print("a is greater than b and c")
elif b>a>c:
    print("b is greater than a and c")

elif c>a>b:
    print("c is greater than a and b")
else:
    print("All numbers are equal")