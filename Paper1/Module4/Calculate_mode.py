"""
Write a function calculate_mode(numbers) from scratch 
that returns the most frequent value (assume single mode, no ties).
"""
def calculate_mode(numbers):
    dict_freq={}
    for i in numbers:
        if i in dict_freq:
            dict_freq[i]+=1
        else:
            dict_freq[i]=1
    max_freq= max(dict_freq.values())
    for key, value in dict_freq.items():
        if max_freq== value:
            return key

data=[1, 40, 3, 3, 40, 5, 40, 40]
print("Calculated Mode: ", calculate_mode(data))