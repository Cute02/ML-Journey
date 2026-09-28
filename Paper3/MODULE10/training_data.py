from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

X_train, X_rest, y_train, y_rest = train_test_split(X, y,
                                                    train_size=0.7, # 70% for training
                                                    random_state=42, # makes shuffle repeatable
                                                    stratify=y)  # keeps each species

print("Total rows: ", len(X))
print("Training: ", len(X_train))
print("Held back rows: ", len(X_rest))