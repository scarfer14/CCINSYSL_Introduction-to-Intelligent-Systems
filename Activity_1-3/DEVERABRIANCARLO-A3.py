# feature_engineer.py
import pandas as pd
import os

# File paths
cleaned_data_path = 'cleaned_evidence.csv'
feature_engineered_path = 'feature_engineered_evidence.csv'

# Check if cleaned data exists
if not os.path.exists(cleaned_data_path):
    print(f"Error: '{cleaned_data_path}' not found. Please complete Week 2 activity first.")
    exit()

# Load cleaned data
df = pd.read_csv(cleaned_data_path)

# Ensure timestamp is datetime (just in case)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create new features
df['hour_of_day'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()
df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])

# Save the new feature-engineered dataset
df.to_csv(feature_engineered_path, index=False)

print(f"Successfully created feature-engineered data: '{feature_engineered_path}'.")
print("\nFirst 5 rows of feature-engineered data:")
print(df.head())
