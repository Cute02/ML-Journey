try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("U have to enter positive number")
except ValueError:
    print()
