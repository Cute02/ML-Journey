"""
Without using any library, write code to detect outliers 
in a dataset using the IQR (Interquartile Range) method.
"""

import pandas as pd
data=[1, 7, 3, 3, 4, 5, 40, 9]
s=pd.Series(data)
Q1=s.quantile(0.25)
Q3=s.quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1 - IQR * 1.5
outer_bound=Q3 + IQR * 1.5
outliers=((s<lower_bound) | (s> outer_bound))
print("Lower bound: ", lower_bound, "Outer_bound: ", outer_bound)
print("Outliers: ",s[outliers.tolist()])