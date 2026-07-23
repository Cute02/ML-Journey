"""
 Write skew_direction(data) that computes mean and median, then returns "right-skewed" if mean > median,
 "left-skewed" if mean < median, else "symmetric". Test it on both Q1's dataset 
 [70, 72, 68, 71, 69, 70, 73, 67, 200] and Q3's dataset [90, 92, 88, 91, 89, 15, 90].
"""

from stats_util import my_mean, my_median

def skew_detection(data):
    if my_mean(data)>my_median(data):
        return "right-skewed"
    elif my_mean(data)<my_median(data):
        return "left-skewed"
    else:
        return "symmetric"

    
print(skew_detection([70, 72, 68, 71, 69, 70, 73, 67, 200]))
print(skew_detection([90, 92, 88, 91, 89, 15, 90]))
