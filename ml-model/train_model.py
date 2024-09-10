import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv('motion_data.csv')

# Features and labels
X = df[['acceleration_x', 'acceleration_y', 'acceleration_z', 'rotation_alpha', 'rotation_beta', 'rotation_gamma']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open('motion_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete. Model saved as 'motion_model.pkl'.")
