# variance=(sum(value-mean)**2)/n
data = [7, 14, 2, 7, 19, 11, 2, 5, 20, 1]
length = len(data)
mean_sum = sum(data)
mean = mean_sum/length
print(mean)
list_diff = []
for i in data:
    diff_square = (i-mean)**2
    list_diff.append(diff_square)
variance = sum(list_diff)/length
std_dev = variance**0.5
print("Standard Deviation = ", std_dev)
