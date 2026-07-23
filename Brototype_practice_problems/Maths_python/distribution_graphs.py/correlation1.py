"""
Write simple_direction_check(pairs) — you already built something close to this in Day 1 (direction). 
Reuse/adapt it to return "positive" or "negative" based on first vs last point.
 Test it on Q1's dataset: [(1,80), (2,76), (3,72), (4,68), (5,64)].
"""

def simple_direction_check(pairs):
    if pairs[0][1]<pairs[-1][1]:
        return "positive"
    if pairs[0][1]>pairs[-1][1]:
        return "negative"
    
print(simple_direction_check([(1,80), (2,76), (3,72), (4,68), (5,64)]))