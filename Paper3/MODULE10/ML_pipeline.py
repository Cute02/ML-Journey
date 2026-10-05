from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import pandas as pd

data= load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)
X.shape, y.shape

# 1. Split data first
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Build the pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')), # Learns median from X_train only
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# 3. Fit and score safely
pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))
