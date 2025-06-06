#Write a program to accept two numbers from the user and swap their values. (Example: x=12, y=15; after swapping x=15, y=12)
x=int(input("Enter a value x:"))
y=int(input("Enter the value y:"))
x,y=y,x
print(f"After swaping:x = {x} and y = {y} ")