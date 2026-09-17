"""
Write independent_and(p_a, p_b) that returns the probability of 
both independent events happening. Test it on Q2's numbers (P(rolling a 6) = 1/6, P(heads) = 1/2).
"""

def independent_and(p_a, p_b):
    return p_a*p_b

print(independent_and(1/6, 1/2))