#print in a square box
# Loop through 3 rows
for i in range(3):
    for j in range(3):
        if i == j:
            print("19", end=" ")
        else:
            print("0", end=" ")
    print()  
