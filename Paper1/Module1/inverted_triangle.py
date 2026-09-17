row = 5
for i in range(row, 0, -1):
    for k in range(1, row-i+1):
        print(" ", end="")
    for j in range(0, (2*i-1)):
        print("*", end="")
    print()
