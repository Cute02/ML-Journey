from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X = [[30,550,3],[45,600,2],[80,750,0],[20,500,4],[95,800,0],[40,620,2],
     [55,680,1],[25,530,3],[70,720,1],[35,590,2]]
y = ["default","default","no_default","default","no_default","no_default",
     "no_default","default","no_default","default"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model= DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print('Test set predictions: ', predictions)
print('Actual labels: ', list(y_test))
print('Accuracy', accuracy_score(y_test, predictions))