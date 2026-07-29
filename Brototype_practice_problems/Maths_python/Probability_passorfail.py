"""
Write a function probability(favorable, total) that returns
 the probability. Then, given this dataset of 15 Brototype students' quiz results:
"""
#  TO FIND PROBABILITY
def probability(favorable, total):
      return favorable/total
#TO FIND FAVORABLE_COUNT
def favorable(results):
    favorable_count=0
    for i in results:
        if i.lower()=="pass":
            favorable_count+=1
    return favorable_count

# TO FIND INDEPENDENT PROBABILITY
def independent(q_a, q_b):
     return q_a*q_b

quiz_a = ["pass", "fail", "pass", "pass", "fail", "pass", "fail", "pass"]
quiz_b = ["fail", "pass", "pass", "fail", "pass", "pass", "pass", "fail"]    
        
p_a=probability(favorable(quiz_a), len(quiz_a))
p_b=probability(favorable(quiz_b), len(quiz_b))

print(f"{p_a} * {p_b} = {p_a*p_b}")

print("independent probability is ", independent(p_a, p_b))