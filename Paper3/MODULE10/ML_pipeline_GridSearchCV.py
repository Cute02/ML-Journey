

import os
import joblib 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.datasets import make_classification # Used here to simulate the heart dataset structure
from sklearn.model_selection import StratifiedKFold, train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline 
from sklearn.feature_selection import SelectKBest, f_classif 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    roc_auc_score, confusion_matrix, classification_report, roc_curve
)
# =====================================================================# 0. SIMULATING THE RAW HEART DISEASE DATASET STRUCTURE# =====================================================================# Creating a dummy dataset to mirror the actual columns for functional execution
X_raw, y_raw = make_classification(
    n_samples=1000, n_features=9, n_informative=7, n_redundant=2, random_state=42
)
columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex', 'cp', 'fbs', 'exang']
df = pd.DataFrame(X_raw, columns=columns)
# Convert some columns into categorical to simulate real raw metrics
df['sex'] = np.where(df['sex'] > 0, 'Male', 'Female')
df['cp'] = np.where(df['cp'] > 0, 'Typical Angina', 'Asymptomatic')
df['fbs'] = np.where(df['fbs'] > 0, 'True', 'False')
df['exang'] = np.where(df['exang'] > 0, 'Yes', 'No')
df['target'] = y_raw
# Separate Target and Features
X = df.drop(columns=['target'])
y = df['target']

print("--- Step 12 & 13: Data Preparation & Stratified Splitting ---")# Define numerical and categorical features
num_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
cat_features = ['sex', 'cp', 'fbs', 'exang']
# Stratified Train-Test Split (80/20) to maintain heart disease target proportions
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, stratify=y, random_state=42
)
print(f"Training shape: {X_train.shape}, Test shape: {X_test.shape}\n")

# =====================================================================# 1. BUILDING PREPROCESSING AND FEATURE SELECTION PIPELINES# =====================================================================# Numerical pipeline: Scale variables to protect distance-based models
num_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])
# Categorical pipeline: Encode labels to continuous numerical flags
cat_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
# Combine preprocessing logic
preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, num_features),
    ('cat', cat_transformer, cat_features)
])

# =====================================================================# 2. STEP 14 & 15: MULTI-MODEL INITIALIZATION & STRATIFIED K-FOLD CV# =====================================================================
print("--- Step 14 & 15: Base Training & Multi-Model Stratified K-Fold CV ---")
base_models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}
# 5-Fold Stratified Cross-Validation scheme to validate generalisation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for name, model in base_models.items():
    # Build a unified pipeline combining Preprocessing -> Feature Selection -> Estimator
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('selector', SelectKBest(score_func=f_classif, k='all')), 
        ('classifier', model)
    ])
    
    cv_scores = []
    # Manual loop iteration to show validation progression across folds
    for train_idx, val_idx in cv.split(X_train, y_train):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
        
        full_pipeline.fit(X_tr, y_tr)
        preds = full_pipeline.predict(X_val)
        cv_scores.append(recall_score(y_val, preds)) # Medical context: prioritize Recall/Sensitivity
        
    print(f"{name} Mean Stratified CV Recall (Sensitivity): {np.mean(cv_scores):.4f}")
print("\n")

# =====================================================================# 3. STEP 17: HYPERPARAMETER TUNING VIA GRIDSEARCHCV# =====================================================================
print("--- Step 17: Model Improvement (GridSearchCV Optimization) ---")
# Let's optimize the Random Forest Classifier
tuning_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('selector', SelectKBest(score_func=f_classif, k='all')),
    ('classifier', RandomForestClassifier(random_state=42))
])
param_grid = {
    'classifier__n_estimators':,
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5, 10]
}
# Grid search optimization targeting Recall score metrics
grid_search = GridSearchCV(
    tuning_pipeline, param_grid, cv=cv, scoring='recall', n_jobs=-1
)
grid_search.fit(X_train, y_train)
best_pipeline = grid_search.best_estimator_
print(f"Optimal Parameters Found: {grid_search.best_params_}\n")

# =====================================================================# 4. STEP 16: ADVANCED MULTI-MODEL EVALUATION METRICS# =====================================================================
print("--- Step 16: Multi-Model Evaluation on Holdout Test Split ---")
y_pred_test = best_pipeline.predict(X_test)
y_prob_test = best_pipeline.predict_proba(X_test)[:, 1]
# Generating core evaluation matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_test))
print(f"\nHoldout Test Accuracy:  {accuracy_score(y_test, y_pred_test):.4f}")
print(f"Holdout Test Precision: {precision_score(y_test, y_pred_test):.4f}")
print(f"Holdout Test Recall:    {recall_score(y_test, y_pred_test):.4f} <-- (Critical Medical Index)")
print(f"Holdout Test F1-Score:  {f1_score(y_test, y_pred_test):.4f}")
print(f"Holdout Test ROC-AUC:   {roc_auc_score(y_test, y_prob_test):.4f}\n")

# =====================================================================# 5. STEP 18: ARTIFACT SERIALIZATION AND PRODUCTION PREDICTION INFERENCE# =====================================================================
print("--- Step 18: Training vs. Prediction (Inference Phase) ---")
# Save the entire operational pipeline layout (scalers, encoders, model weights)
model_filename = 'heart_disease_production_model.joblib'
joblib.dump(best_pipeline, model_filename)
print(f"Production pipeline successfully saved to '{model_filename}'")
# --- SIMULATING THE PRODUCTION PREDICT SCRIPT ENVIRONMENT ---# Load the saved model artifact cleanly back into memory
deployed_pipeline = joblib.load(model_filename)
# Create a mock raw single row patient incoming record (No manual transformations applied yet)
new_patient_data = pd.DataFrame([{
    'age': 58,
    'trestbps': 135,
    'chol': 240,
    'thalach': 162,
    'oldpeak': 1.8,
    'sex': 'Male',
    'cp': 'Typical Angina',
    'fbs': 'False',
    'exang': 'Yes'
}])
# Execute prediction using the fully standalone pipeline
raw_prediction = deployed_pipeline.predict(new_patient_data)
raw_probabilities = deployed_pipeline.predict_proba(new_patient_data)

print("\n--- Live Production Patient Inference Result ---")
print(f"Raw Input: Presenting clinical metrics for single evaluation record.")
print(f"Model Diagnostic Classification output: {raw_prediction[0]} (where 1 = Heart Disease Presence, 0 = Healthy)")
print(f"Calculated Probability Matrix: Healthy: {raw_probabilities[0][0]:.4f} vs Heart Disease: {raw_probabilities[0][1]:.4f}")
# Adjust threshold behavior explanation for custom clinical safety constraints
custom_safety_threshold = 0.35
custom_prediction = 1 if raw_probabilities[0][1] >= custom_safety_threshold else 0
print(f"Adjusted Safety Decision (Threshold lowered to {custom_safety_threshold}): {custom_prediction}")
# Clean up artifact file
if os.path.exists(model_filename):
    os.remove(model_filename)



