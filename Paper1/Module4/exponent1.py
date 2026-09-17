"""
 Write a function exponential(x, a, b) that returns a * (b**x). 
 Test it on the bacteria example: a=50, b=2, x=3 (should give 400).
"""

def exponential(x,a,b):
    return a*(b**x)
print(exponential(3,50, 2))