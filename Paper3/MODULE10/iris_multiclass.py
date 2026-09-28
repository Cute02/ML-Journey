from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris=load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
model=LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

sample = X_test[:1]
print("*"* 20)
print("Predicted class: ", iris.target_names[model.predict(sample)[0]])
print("Class order: ", list(iris.target_names))
print('probabilities', model.predict_proba(sample).round(3))
