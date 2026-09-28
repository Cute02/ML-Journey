import numpy as np
from sklearn.linear_model import LinearRegression

# Monthly sales for 12 months, with an upward trend
sales = np.array([100, 104, 109, 113, 118, 121, 127, 131, 135, 140, 144, 149])
X = np.array([sales[i:i+2] for i in range(len(sales)-2)])
y = sales[2:]

X_train, X_test = X[:-3], X[-3:]
y_train, y_test = y[:-3], y[-3:]


model=LinearRegression().fit(X_train, y_train)

print("Predicted: ", model.predict(X_test).round(1))
print("Actual: ", y_test)

print("Forecast for next month: ", model.predict([sales[-2:]]).round(1))