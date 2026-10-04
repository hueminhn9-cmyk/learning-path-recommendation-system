import numpy as np
import tensorflow as tf
import joblib

# Load models
model = tf.keras.models.load_model("model/student_model.h5")
scaler = joblib.load("model/scaler.pkl")
level_map = joblib.load("model/level_map.pkl")

print(f"Level Map: {level_map}")

def predict(marks, interest, time_spent):
    # interest: Low=1, Medium=2, High=3
    input_data = np.array([[marks, interest, time_spent]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled, verbose=0)
    predicted_class = np.argmax(prediction[0])
    level = level_map.get(predicted_class, "Unknown")
    return level

test_cases = [
    (30, 1, 1.0), # Beginner
    (60, 2, 2.0), # Intermediate
    (90, 3, 4.0), # Advanced
]

for m, i, t in test_cases:
    print(f"Marks: {m}, Interest: {i}, Time: {t} -> Predicted: {predict(m, i, t)}")
