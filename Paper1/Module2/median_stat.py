data = [7, 14, 2, 7, 19, 11, 2, 5, 20, 1]
data.sort()
length = len(data)
mid = int(length/2)
# for i in data:
#    print(i)
if length % 2 == 0:
    print((data[mid-1]+data[mid])/2)
else:
    print(data[mid])
