"""
Write bayes_theorem(p_b_given_a, p_a, p_b) implementing the Bayes formula.
Test it on Q4's numbers — P(flagged | defective) = 0.95, P(defective) = 0.02, P(flagged) = 0.05.
"""
def bayes_thrm(p_b_given_a, p_a, p_b):
    return (p_b_given_a*p_a)/p_b
print(bayes_thrm(0.95, 0.02, 0.05))
