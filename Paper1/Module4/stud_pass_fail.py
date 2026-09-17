"""
 Now write it as code. You'll need a function that loops through students, and for each one checks:
 does attended == "full"? If yes, bump a full_count. Does it also have result == "pass"? 
 If yes, bump a full_and_pass_count. Then divide. Give it a shot.
"""

def full_pass(students):
    full=0
    full_and_pass=0
    for i in range(len(students)):
        if students[i]["attended"]=="full":
            full+=1
            if students[i]["result"]=="pass":
                full_and_pass+=1
    return full_and_pass/full
    

students = [
    {"attended": "full", "result": "pass"},
    {"attended": "full", "result": "pass"},
    {"attended": "partial", "result": "fail"},
    {"attended": "full", "result": "fail"},
    {"attended": "partial", "result": "pass"},
    {"attended": "full", "result": "pass"},
    {"attended": "partial", "result": "fail"},
    {"attended": "full", "result": "pass"},
    {"attended": "partial", "result": "fail"},
    {"attended": "full", "result": "pass"},
]

print(full_pass(students))