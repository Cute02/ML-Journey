"""
Write conditional_prob(event_and_condition_count, condition_count) that 
computes conditional probability from raw counts. Test it on both parts of Q3 — 
practiced (28 out of 35) and didn't practice (5 out of 15).
"""
def conditional_prob(event_and_condition_count, condition_count):
    return event_and_condition_count/condition_count
print(conditional_prob(28,35))
print(conditional_prob(5,15))