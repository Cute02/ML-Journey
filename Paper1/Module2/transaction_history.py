def category_totals(transactions):
    totals={}
    for record in transactions:
        cat=record["category"]
        amt=record["amount"]
        if cat in totals:
            totals[cat]+=amt
        else:
            totals[cat]=amt
    return totals

transactions = [
    {"id": 1, "category": "food", "amount": 250},
    {"id": 2, "category": "travel", "amount": 1200},
    {"id": 3, "category": "food", "amount": 150},
    {"id": 4, "category": "shopping", "amount": 800},
    {"id": 5, "category": "travel", "amount": 300},
    {"id": 5, "category": "travel", "amount": 300},
]
print(category_totals(transactions))
