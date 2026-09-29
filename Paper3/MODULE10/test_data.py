from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

X_train, X_hold, y_train, y_hold = train_test_split(X, y, 
                                                    train_size=0.6, 
                                                    random_state=42, 
                                                    stratify=y)

X_val, X_test, y_val, y_test = train_test_split(X_hold, y_hold,
                                                 test_size=0.5,
                                                   random_state=41, 
                                                   stratify=y_hold)

best_depth, best_score = None, -1
for depth in [1, 2,3, 4, 5]:
    model=DecisionTreeClassifier(max_depth=depth, random_state=0)
    model.fit(X_train, y_train)
    score= model.score(X_val, y_val)
    if score>best_score:
        best_depth, best_score = depth, score

final_model = DecisionTreeClassifier(max_depth=best_depth, random_state=0)
final_model.fit(X_train, y_train)
print("Chosen max_depth: ", best_depth)
print("Final test accuracy: ", round(final_model.score(X_test, y_test),2))
