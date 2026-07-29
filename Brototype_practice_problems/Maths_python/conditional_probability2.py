"""
Write a function conditional_probability(students, condition_key, event_key) 
that computes P(passed | submitted_early) — general enough that it counts 
(condition AND event) divided by (condition), by looping through the list once. Test it on this dataset.
"""

def conditional_probability(students, condition_key, event_key):
    both_count=0
    early_count=0
    for i in students:
        if i[condition_key]==True:
            early_count+=1
            if i[ event_key]==True:
                both_count+=1

    return both_count/early_count

students = [
    {"submitted_early": True, "passed": True},
    {"submitted_early": True, "passed": True},
    {"submitted_early": False, "passed": False},
    {"submitted_early": True, "passed": False},
    {"submitted_early": False, "passed": True},
    {"submitted_early": True, "passed": True},
    {"submitted_early": False, "passed": False},
    {"submitted_early": True, "passed": True},
    {"submitted_early": False, "passed": False},
    {"submitted_early": True, "passed": True},
]

print(conditional_probability(students, "submitted_early","passed"))
