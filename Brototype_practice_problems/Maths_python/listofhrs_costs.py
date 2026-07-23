def total_cost(hours):
    cost=[x*80 +150 for x in hours ]
    return cost
print(total_cost([0, 3, 6, 9]))