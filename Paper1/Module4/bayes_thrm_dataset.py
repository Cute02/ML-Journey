items = [
    {"actual": "defective", "flagged": "yes"},
    {"actual": "good", "flagged": "no"},
    {"actual": "good", "flagged": "yes"},
    {"actual": "defective", "flagged": "yes"},
    {"actual": "good", "flagged": "no"},
    # ... imagine this list has 200 entries total
]

def bayes_theorem(items):
    flagged_defective=0
    flagged=0
    defective=0
    total_items=len(items)
    for i in range(total_items):
        if items[i]["actual"]=="defective" and items[i]["flagged"]=="yes":
            flagged_defective+=1
        if items[i]["flagged"] == "yes":
            flagged+=1
        if items[i]["actual"]=="defective":
            defective+=1

    p_d = defective/total_items
    p_fd = flagged_defective/defective
    p_f = flagged/total_items
    p_d_f=(p_fd*p_d)/p_f
    return p_d_f
print(bayes_theorem(items))