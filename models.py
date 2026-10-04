import os
import json
import joblib
import streamlit as st

try:
    import tensorflow as tf
except Exception:
    tf = None

@st.cache_resource
def load_models():
    model = None
    model_type = "none"
    scaler = None
    level_map = {0: "Beginner", 1: "Intermediate", 2: "Advanced"}
    metrics = []

    if os.path.exists("model/scaler.pkl"):
        try:
            scaler = joblib.load("model/scaler.pkl")
        except Exception:
            scaler = None

    if os.path.exists("model/level_map.pkl"):
        try:
            level_map = joblib.load("model/level_map.pkl")
        except Exception:
            pass

    if os.path.exists("model/model_metrics.json"):
        try:
            with open("model/model_metrics.json", "r") as f:
                metrics = json.load(f)
        except Exception:
            metrics = []

    if tf is not None and os.path.exists("model/student_model.h5"):
        try:
            model = tf.keras.models.load_model("model/student_model.h5")
            model_type = "keras"
        except Exception:
            model = None

    if model is None and os.path.exists("model/sklearn_model.pkl"):
        try:
            model = joblib.load("model/sklearn_model.pkl")
            model_type = "sklearn"
        except Exception:
            model = None

    return model, model_type, scaler, level_map, metrics

def interest_to_number(interest):
    return {"Low": 1, "Medium": 2, "High": 3}.get(interest, 2)
