rows = int(input("Enter the number of rows: "))

i = 1
while i <= rows:
    # leading spaces to center the pyramid
    j = 1
    while j <= rows-i:
        print(" ", end="")
        j += 1

    k = 1
    while k <= 2*i-1:
        print("*", end="")
        k += 1
    print()
    i += 1
