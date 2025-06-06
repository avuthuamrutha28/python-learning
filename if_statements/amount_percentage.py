#Write a program to accept the bill amount and age of the customer; if the customer’s age is >50 years then give a discount of 5% on the bill.
amount=float(input("Enter a amount:"))
age=int(input("Enter Age:"))
if age>50:
    discount=amount*0.05
    bill=amount-discount
else:
    bill=amount

print(f"The bill amount is {bill}")
