"""
Question 6: Write detect_outliers(data, threshold) that returns a list of values whose distance 
from the mean is greater than threshold. Test it on Q3's dataset [90, 92, 88, 91, 89, 15, 90] with 
threshold = 20.
Think through the steps first:

Find the mean of the data.
Loop through each value, and check: is its distance from the mean (use abs(value - mean)) 
greater than the threshold? If yes, add it to a results list.
"""
from stats_util import my_mean
def detect_outliers(data, threshold):
    results=[]
    for value in data:
        if abs(value-my_mean(data))>=threshold:
            results.append(value)
    return results

