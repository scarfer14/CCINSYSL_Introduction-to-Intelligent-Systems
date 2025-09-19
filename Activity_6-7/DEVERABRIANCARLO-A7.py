# malware_classifier.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# De Vera, Brian Carlo A.
# Step 1: Simulated Dataset
# ======================

data = {
    "file_size":    [200, 4500, 120, 8000, 300, 9000, 150, 7000],
    "entropy":      [3.2, 7.8, 2.1, 8.5, 4.0, 8.9, 2.5, 7.2],
    "num_imports":  [10, 50, 5, 60, 12, 55, 8, 62],
    "section_count":[3, 8, 2, 10, 4, 12, 2, 9],
    "label":        ["Benign", "Malware", "Malware", "Malware", 
                     "Benign", "Malware", "Benign", "Malware"]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

# De Vera, Brian Carlo A.
# Step 2: Train-Test Split (Stratified)
# ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)

# De Vera, Brian Carlo A.
# Step 3: Train Model
# ======================
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)


# De Vera, Brian Carlo A.
# Step 4: Evaluate Model
# ======================
y_pred = clf.predict(X_test)
print("=== Classification Report ===")
print(classification_report(y_test, y_pred, zero_division=0))
