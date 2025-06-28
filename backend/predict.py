import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image

# Load model and label map
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/model.h5')
LABEL_MAP_PATH = os.path.join(os.path.dirname(__file__), '../model/label_map.json')

model = load_model(MODEL_PATH)

with open(LABEL_MAP_PATH, 'r') as f:
    label_map = json.load(f)

# Reverse the label map: index -> class
reverse_label_map = {v: k for k, v in label_map.items()}

# Prediction function
def predict_image(image_path, target_size=(128, 128)):
    try:
        # Load and preprocess image
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_label = reverse_label_map[predicted_index]
        confidence = float(np.max(predictions[0]))

        return {
            "prediction": predicted_label,
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        return {"error": str(e)}
