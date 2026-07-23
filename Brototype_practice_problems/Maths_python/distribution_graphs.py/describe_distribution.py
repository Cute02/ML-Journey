"""
write describe_distribution(data, outlier_threshold) that prints the mean, median, skew direction,
 and any detected outliers. Test it on submission_times = [2, 3, 3, 4, 2, 3, 5, 3, 4, 40].
"""
from stats_util import my_mean, my_median
import outlier_detection, skew_detection
def describe_distribution(data, outlier_threshold):
    print("Mean:", my_mean(data))
    print("Median:", my_median(data))
    print("Outliers:", outlier_detection.detect_outliers(data, outlier_threshold))
    print("Skew: ", skew_detection.skew_detection(data))




print(describe_distribution([2, 3, 3, 4, 2, 3, 5, 3, 4, 40], 20))