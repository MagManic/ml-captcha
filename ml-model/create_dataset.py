import pandas as pd

# Create a sample dataset (you can replace this with real data)
data = {
    'acceleration_x': [2.5, 0.3, 1.1, 2.8, 0.1],
    'acceleration_y': [1.1, 0.1, 0.3, 0.9, 0.2],
    'acceleration_z': [0.9, 0.2, 2.5, 0.5, 0.1],
    'rotation_alpha': [0.5, 0.3, 0.1, 1.0, 0.2],
    'rotation_beta': [0.4, 0.1, 0.2, 0.6, 0.3],
    'rotation_gamma': [0.6, 0.2, 0.3, 0.5, 0.4],
    'label': ['human', 'bot', 'human', 'human', 'bot']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('motion_data.csv', index=False)

print("Dataset created successfully and saved to 'motion_data.csv'")
