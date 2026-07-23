"""
Without using any library, write a Python function 
calculate_mean(numbers) that takes a list and returns the mean.
"""

def calculate_mean(data):
    total=0
    for i in data:
        total+=i
    return total/len(data)

data=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
print("Mean calculated is ", calculate_mean(data))