import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image
import os

# Paths
MODEL_PATH = "model/model.h5"
LABEL_MAP_PATH = "model/label_map.json"
IMG_SIZE = (128, 128)

# Load model and label map
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    with open(LABEL_MAP_PATH, 'r') as f:
        label_map = json.load(f)
    reverse_map = {v: k for k, v in label_map.items()}
    return model, reverse_map

model, label_map = load_model()

# UI
st.title("🗑️ Garbage Classification")
st.markdown("Upload an image of garbage and let the model predict the type.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess
    img = image.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = prediction[0][class_index] * 100
    predicted_label = label_map[class_index]

    st.success(f"Predicted: **{predicted_label}**")
    st.info(f"Confidence: **{confidence:.2f}%**")
