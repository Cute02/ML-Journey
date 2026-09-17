"""
Write a function calculate_variance(numbers) from scratch.
"""


def calculate_variance(data):
    total=0
    length=len(data)
    for j in data:
        total+=j
    my_mean=total/length
    squared_diff=0

    for i in data:
        squared_diff+=(i-my_mean)**2
    var=squared_diff/length
    return var

data=[12, 15, 12, 18, 20, 12, 90]
var_func=calculate_variance(data)
print("Variance is ", var_func)
print("Standard Deviation is ", var_func**0.5)
