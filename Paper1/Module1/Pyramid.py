rows = 6
for i in range(rows, 0, -1):
    for j in range(1, rows-i+1):
        print(" ", end="")
    for k in range(0, (2*i-1)):
        print("*", end="")
    print()
