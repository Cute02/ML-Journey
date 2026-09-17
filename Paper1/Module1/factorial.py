num = int(input("Enter the number to get its factorial: "))
f = 1
for i in range(1, num+1):
    f *= i
print(f"Factorial of {num} is {f}")
