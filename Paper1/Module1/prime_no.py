# Prime numbers from 1 to 20
num = int(input("Enter the limit"))

print("Prime numbers are")
for i in range(2, num+1):
    prime = 0
    for j in range(2, int(i/2)):
        if i % j == 0:
            prime = 1
            break
    if prime == 0:
        print(i)
