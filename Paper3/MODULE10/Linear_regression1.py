from sklearn.linear_model import LinearRegression

X= [[1], [2], [3], [4], [5], [6]]
y = [12, 18, 24, 31, 36, 42]

model=LinearRegression()
model.fit(X, y)

print("Prediction for 3.5km: ", model.predict([[3.5]]))
print("Prediction for 10km:", model.predict([[10]]))

print('Slope (minutes per km): ', model.coef_)
print('Intercept: ', model.intercept_)