#Write a program to accept the weight of 5 persons (one by one) and display the net weight and the average weight.
total_weight=0
for i in range(1,6):
    weight=float(input(f"Enter a person weight {i} in kg: "))
    total_weight+=weight
    avg_weight=total_weight/5
print(f"The total weight is: {total_weight} kg")
print(f"The avg weight is:{avg_weight} kg")