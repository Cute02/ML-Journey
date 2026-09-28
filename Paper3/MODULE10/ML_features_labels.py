import pandas as pd

df = pd.DataFrame({
    "size_sqft":  [800, 1200, 1500, 2000],
    "bedrooms":   [2, 3, 3, 4],
    "price_lakh": [40, 60, 72, 95],
})

X=df[['size_sqft', 'bedrooms']]
y= df['price_lakh']

print(X)
print(y)