#If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made a profit or incurred a loss. Also determine the quantum of profit or loss.
selling_price=int(input("Enter the selling price:"))
cost_price=int(input("Enter the cost price"))
if selling_price>cost_price:
    print("Got profit")
elif selling_price<cost_price:
    print("Got lose")
else:
    print("No profit, No lose")
