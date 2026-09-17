# FIBONACCI SERIES
num = int(input("Enter the limit: "))
first = 0
second = 1
print(first, end="\n")
print(second, end="\n")
for i in range(num):
    third = first+second
    print(third, end="\n")
    first = second
    second = third
