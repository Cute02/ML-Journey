quiz_a_results = ["pass", "fail", "pass", "pass", "fail", "pass", "fail", "pass", "pass", "pass"]
quiz_b_results = ["pass", "pass", "fail", "pass", "pass", "fail", "pass", "pass", "fail", "pass"]

def count_targets(quiz):
    favourable=0
    for i in quiz:
        if i.lower()=="pass":
            favourable+=1
    print(favourable)
    return favourable
    

def independent_and(p_a, p_b):
    return p_a*p_b

p_a=count_targets(quiz_a_results)/len(quiz_a_results)
p_b=count_targets(quiz_b_results)/len(quiz_b_results)

print("p_a: ", p_a)
print("p_b: ", p_b)

print("Independent probability", independent_and(p_a, p_b))
