import sys
import json
import pickle
import numpy as np

# Load the trained ML model
with open('motion_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Get motion data from the command-line argument
data = json.loads(sys.argv[1])

# Extract acceleration and rotation values
X_new = np.array([[data['acceleration']['x'], data['acceleration']['y'], data['acceleration']['z'],
                   data['rotationRate']['alpha'], data['rotationRate']['beta'], data['rotationRate']['gamma']]])

# Predict using the ML model
prediction = model.predict(X_new)

# Output the result (either 'human' or 'bot')
print(prediction[0])
