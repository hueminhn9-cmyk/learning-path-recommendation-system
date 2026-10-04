import os
import json
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Ensure directories exist
os.makedirs("dataset", exist_ok=True)
os.makedirs("model", exist_ok=True)

print("[INFO] Generating 5,000 Multi-Subject Student Academic Dataset Samples...")

np.random.seed(42)
n_rows = 5000

subjects = [
    "Machine Learning", 
    "Data Science", 
    "Cybersecurity", 
    "Web Development", 
    "Cloud Computing", 
    "Artificial Intelligence",
    "Mobile App Development",
    "Software Engineering",
    "Database Systems",
    "Computer Networks"
]

subject_data = np.random.choice(subjects, n_rows)
marks = np.random.randint(0, 101, n_rows)

interest_levels = []
interest_nums = []
time_spent = []

for m in marks:
    # Add realistic distribution & variation
    noise_interest = np.random.choice([-1, 0, 1], p=[0.1, 0.8, 0.1])
    noise_time = np.random.uniform(-0.8, 0.8)
    
    if m <= 45:
        base_interest = 1
        base_time = 1.5
    elif m <= 75:
        base_interest = 2
        base_time = 3.5
    else:
        base_interest = 3
        base_time = 6.0
        
    i_num = int(np.clip(base_interest + noise_interest, 1, 3))
    t_val = round(float(np.clip(base_time + noise_time, 0.5, 10.0)), 1)
    
    i_str = {1: "Low", 2: "Medium", 3: "High"}[i_num]
    
    interest_nums.append(i_num)
    interest_levels.append(i_str)
    time_spent.append(t_val)

# Create DataFrame
df = pd.DataFrame({
    'Student_ID': [f"SV{i+1000:04d}" for i in range(n_rows)],
    'Subject': subject_data,
    'Marks': marks,
    'Interest': interest_levels,
    'Interest_Score': interest_nums,
    'Time_Spent_Hours': time_spent
})

df.to_csv('dataset/students.csv', index=False)
print(f"[OK] Saved expanded dataset with {len(df)} rows to 'dataset/students.csv'!")

# 2. Features & Labels Generation using K-Means clustering anchor
X = np.column_stack((marks, interest_nums, time_spent))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

cluster_means = [np.mean(marks[cluster_labels == k]) for k in range(3)]
sorted_indices = np.argsort(cluster_means)
remapping = {old_idx: new_idx for new_idx, old_idx in enumerate(sorted_indices)}
y_labels = np.array([remapping[label] for label in cluster_labels])
level_map = {0: "Beginner", 1: "Intermediate", 2: "Advanced"}

# 3. Train / Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_labels, test_size=0.20, random_state=42, stratify=y_labels)

print(f"[INFO] Dataset split: {len(X_train)} Training Samples, {len(X_test)} Testing Samples.")

# 4. Train Keras Deep Learning ANN Model
print("[INFO] Training Keras Deep ANN Model...")
ann_model = Sequential([
    Dense(32, activation='relu', input_shape=(3,)),
    Dropout(0.1),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')
])

ann_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
ann_model.fit(X_train, y_train, epochs=40, batch_size=32, validation_data=(X_test, y_test), verbose=0)

ann_test_preds = np.argmax(ann_model.predict(X_test, verbose=0), axis=1)

# 5. Train Benchmark Classifiers
print("[INFO] Training Random Forest Classifier...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

print("[INFO] Training Decision Tree Classifier...")
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

print("[INFO] Training Support Vector Machine (SVM)...")
svm_model = SVC(probability=True, random_state=42)
svm_model.fit(X_train, y_train)
svm_preds = svm_model.predict(X_test)

# 6. Evaluation Metrics Calculation
def get_metrics(name, y_true, y_pred):
    return {
        "model": name,
        "accuracy": round(float(accuracy_score(y_true, y_pred) * 100), 2),
        "precision": round(float(precision_score(y_true, y_pred, average='weighted') * 100), 2),
        "recall": round(float(recall_score(y_true, y_pred, average='weighted') * 100), 2),
        "f1_score": round(float(f1_score(y_true, y_pred, average='weighted') * 100), 2),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist()
    }

metrics_summary = [
    get_metrics("Artificial Neural Network (Keras ANN)", y_test, ann_test_preds),
    get_metrics("Random Forest Classifier", y_test, rf_preds),
    get_metrics("Decision Tree Classifier", y_test, dt_preds),
    get_metrics("Support Vector Machine (SVM)", y_test, svm_preds)
]

# 7. Save Models and Metadata
ann_model.save("model/student_model.h5")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(level_map, "model/level_map.pkl")

with open("model/model_metrics.json", "w") as f:
    json.dump(metrics_summary, f, indent=2)

print("\n[SUCCESS] All models trained on 5,000 samples and metrics saved to model/model_metrics.json.")
print(json.dumps(metrics_summary, indent=2))
