lst = [23, 77, 1, 67, 34, 90, 54]
largest = lst[0]
for i in lst:
    if i > largest:
        second = largest
        largest = i
print(f"Second largest number in the list is {second}")
