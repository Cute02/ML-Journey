"""
Write a function quadratic(x, a, b, c) that returns a*x**2 + b*x + c. 
Test it on x = -2, 0, 2 with a=2, b=0, c=1, and confirm it matches (9, 1, 9).
"""

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c
print(quadratic(-2, 2,0,1))
print(quadratic(0, 2,0,1))
print(quadratic(2, 2,0,1))

