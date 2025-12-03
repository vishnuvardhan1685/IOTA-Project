import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib

# Load the CSV file
print("Loading data...")
df = pd.read_csv('Soil Moisture, Air Temperature and humidity, and Water Motor onoff Monitor data.AmritpalKaur.csv')

# Display basic information
print("\n" + "="*60)
print("DATA OVERVIEW")
print("="*60)
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))
print(f"\nData types:")
print(df.dtypes)
print(f"\nMissing values:")
print(df.isnull().sum())
print(f"\nStatistical summary:")
print(df.describe())

# Check target variable distribution
print("\n" + "="*60)
print("TARGET VARIABLE DISTRIBUTION (Pump Data)")
print("="*60)
print(df['Pump Data'].value_counts())
print(f"\nPercentage distribution:")
print(df['Pump Data'].value_counts(normalize=True) * 100)

# Prepare features and target
X = df[['Soil Moisture', 'Temperature', 'Air Humidity']]
y = df['Pump Data']

# Split the data
print("\n" + "="*60)
print("SPLITTING DATA")
print("="*60)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# Scale the features for better performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Logistic Regression model
print("\n" + "="*60)
print("TRAINING LOGISTIC REGRESSION MODEL")
print("="*60)
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)
print("Model training completed!")

# Make predictions
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)

# Evaluate the model
print("\n" + "="*60)
print("MODEL EVALUATION")
print("="*60)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Pump OFF (0)', 'Pump ON (1)']))

# Display feature coefficients
print("\n" + "="*60)
print("FEATURE IMPORTANCE (Coefficients)")
print("="*60)
feature_names = ['Soil Moisture', 'Temperature', 'Air Humidity']
coefficients = model.coef_[0]
for feature, coef in zip(feature_names, coefficients):
    print(f"{feature}: {coef:.4f}")

# Save the model and scaler
print("\n" + "="*60)
print("SAVING MODEL")
print("="*60)
joblib.dump(model, 'pump_prediction_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Model saved as 'pump_prediction_model.pkl'")
print("Scaler saved as 'scaler.pkl'")

print("\n" + "="*60)
print("MODEL TRAINING COMPLETE!")
print("="*60)
