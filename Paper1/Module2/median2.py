lst = [23, 77, 1, 67, 34, 89, 90, 54]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[j] > lst[i]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)

length = len(lst)
mid = length//2
print(lst[mid])
if len(lst) % 2 == 0:
    median_val = (lst[mid-1] + lst[mid])/2
else:
    median_val = lst[length//2]
print(median_val)
