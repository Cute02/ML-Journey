limit = 100
for i in range(1, 100):
    isPrime = 0
    if i == 1:
        isPrime = 1
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            isPrime = 1
            break
    if (isPrime == 0):
        print(i)
