#print the righthanded triangle
current = 1
rows = [1, 2, 4, 4]

for count in rows:
    for _ in range(count):
        print(current, end=" ")
        current += 1
    print()  
