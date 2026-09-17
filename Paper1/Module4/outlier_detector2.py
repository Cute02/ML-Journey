# Method 2

def calculate_outliers(data):
    data = sorted(data)
    n = len(data)
    
    # Q1 = median of lower half, Q3 = median of upper half
    def median(lst):
        length = len(lst)
        mid = length // 2
        if length % 2 == 0:
            return (lst[mid-1] + lst[mid]) / 2
        else:
            return lst[mid]
    
    lower_half = data[:n//2]
    upper_half = data[(n+1)//2:]
    
    Q1 = median(lower_half)
    Q3 = median(upper_half)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers

data = [1, 7, 3, 3, 4, 5, 40, 9]
print("Outliers:", calculate_outliers(data))