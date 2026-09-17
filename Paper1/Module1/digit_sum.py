num = 1238431255
total_digits = 0
while num > 0:
    last = num % 10
    total_digits += last
    num //= 10
print("Sum of digits: ", total_digits)
