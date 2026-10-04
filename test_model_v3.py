import numpy as np
import tensorflow as tf
import joblib

# Load models
model = tf.keras.models.load_model("model/student_model.h5")
scaler = joblib.load("model/scaler.pkl")
level_map = joblib.load("model/level_map.pkl")

with open('test_outputs_v2.txt', 'w') as f:
    f.write(f"Level Map: {level_map}\n")

    def predict(marks, interest, time_spent):
        # interest: Low=1, Medium=2, High=3
        input_data = np.array([[marks, interest, time_spent]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled, verbose=0)
        predicted_class = np.argmax(prediction[0])
        level = level_map.get(predicted_class, "Unknown")
        return level

    test_cases = [
        (10, 1, 0.5), 
        (20, 1, 1.0),
        (30, 1, 1.5),
        (40, 2, 2.0),
        (50, 2, 2.5),
        (60, 2, 3.0),
        (70, 3, 3.5),
        (80, 3, 4.0),
        (90, 3, 5.0),
    ]

    for m, i, t in test_cases:
        f.write(f"Marks: {m}, Interest: {i}, Time: {t} -> Predicted: {predict(m, i, t)}\n")
