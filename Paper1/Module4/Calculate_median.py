"""
Write a function calculate_median(numbers) from scratch 
— handle both even and odd length lists.
"""

def calculate_median(data):
    length=len(data)
    for i in range(length):
        for j in range(i+1, length):
            if data[i]>data[j]:
                data[i], data[j]=data[j],data[i]
    mid=length//2
    if length%2==0:
        return (data[mid]+data[mid-1])/2
    else:
        return data[mid]
data=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,55, 60, 60]
print("Calculated median is ", calculate_median(data))