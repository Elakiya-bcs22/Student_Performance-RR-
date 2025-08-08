# train_model.py
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Load dataset
df = pd.read_csv('data (5).csv')  # Ensure the file is named correctly

# Features and target
X = df[['hours_per_week', 'num_assignments', 'discussion_posts', 'video_watched', 'logins']]
y = df['completed']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Ridge Regression model
model = Ridge(alpha=1.0)
model.fit(X_train_scaled, y_train)

# Save the model and scaler
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model and scaler saved successfully.")
