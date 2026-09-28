from sklearn.linear_model import LinearRegression

# Independent variable: hours studied. Dependent variable: exam score.
hours = [[1], [2], [3], [4], [5]]     # independent: the input we vary
score = [35, 45, 55, 66, 75]          # dependent: the outcome that responds

model = LinearRegression().fit(hours, score)

for h  in [2, 6, 8]:
    print(h, 'hours -> predicted score: ', round(model.predict([[h]])[0], 1))