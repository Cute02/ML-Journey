num = int(input("Enter a number: "))
Prime = 0
if num == 1:
    Prime = 0
for j in range(2, int(num/2)):
    if num % j == 0:
        Prime = 1
        break
if Prime == 0:
    print("The entered number is prime...")
else:
    print("The entered number is not prime...")
