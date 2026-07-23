"""
Write a function is_symmetric_ish(data, tolerance) that computes mean and median 
(reuse your my_mean and my_median functions), then returns True if abs(mean - median) <= tolerance, else False. 
Test it on Q1's dataset [70, 72, 68, 71, 69, 70, 73, 67, 200] with tolerance = 5.
"""
from stats_util import my_mean, my_median
def is_symmetric_ish(data, tolerance):
    if abs(my_mean(data)-my_median(data))<=tolerance:
        return True
    return False
data=[70, 72, 68, 71, 69, 70, 73, 67, 200]
print(is_symmetric_ish(data, 5))
