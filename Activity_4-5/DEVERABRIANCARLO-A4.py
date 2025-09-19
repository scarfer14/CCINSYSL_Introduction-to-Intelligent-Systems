import pandas as pd
import os
from sklearn.ensemble import IsolationForest

# File paths
feature_engineered_path = 'feature_engineered_evidence.csv'
output_path = 'anomalies_detected_evidence.csv'

# Check if feature-engineered file exists
if not os.path.exists(feature_engineered_path):
    print(f"Error: '{feature_engineered_path}' not found.")
    exit()

# Load the feature-engineered data
df = pd.read_csv(feature_engineered_path)

# Select only numeric features for Isolation Forest
numeric_df = df.select_dtypes(include=['int64', 'float64']).copy()

# Ensure there are numeric features
if numeric_df.empty:
    print("Error: No numeric features found for anomaly detection.")
    exit()

# Increase contamination to make anomalies more likely to be flagged
iso_forest = IsolationForest(
    contamination=0.45,  # Detect ~15% anomalies
    random_state=42,
    n_estimators=200,
    max_samples='auto'
)

# Fit and predict anomalies
pred = iso_forest.fit_predict(numeric_df)

# Keep the original Isolation Forest convention: -1 = anomaly, 1 = normal
df['is_anomaly'] = pred

# Save the new dataset with anomaly labels
df.to_csv(output_path, index=False)

print(f"Anomaly detection completed. File saved as '{output_path}'.")
print("\nAnomaly column distribution:")
print(df['is_anomaly'].value_counts())
