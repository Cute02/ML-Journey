import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

df = pd.DataFrame({
    "customer_id":  [101, 102, 103, 104, 105, 106],
    "income":       [30, 45, 80, 20, 95, 40],
    "credit_score": [550, 600, 750, 500, 800, 620],
    "existing_loans": [3, 2, 0, 4, 0, 2],
    "shoe_size":    [8, 9, 7, 8, 9, 8],       # irrelevant to loan default
    "default":      [1, 1, 0, 1, 0, 0],
})

X = df[["customer_id", 'income', 'credit_score', 'existing_loans', 'shoe_size']]
y = df['default']

selector = SelectKBest(score_func=f_classif, k=2)
selector.fit(X, y)
 
scores= pd.Series(selector.scores_, index=X.columns)
print(scores.sort_values(ascending=False))
print("\nSelected features: ", X.columns[selector.get_support()].tolist())