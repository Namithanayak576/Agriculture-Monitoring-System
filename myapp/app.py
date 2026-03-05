import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
import os

# Define model paths
model_paths = {
    'corn': r'D:\Major project\myproject\models\corn_disease_model (2).h5',
    'potato': r'D:\Major project\myproject\models\potato_model.h5',
    'rice': r'D:\Major project\myproject\models\rice1_disease_model.h5',
    'wheat': r'D:\Major project\myproject\models\wheat1_disease_model.h5',
    'sugarcane': r'D:\Major project\myproject\models\sugarcane1_disease_model.h5',
}

# Define class labels
class_labels = {
    'corn': ["Common Rust", "Gray Leaf Spot", "Healthy", "Northern Leaf Blight"],
    'potato': ["Early Blight", "Healthy", "Late Blight"],
    'rice': ["Brown Spot", "Healthy", "Leaf Blast", "Neck Blast"],
    'wheat': ["Brown Rust", "Healthy", "Yellow Rust"],
    'sugarcane': ["Red Rot", "Healthy", "Bacterial Blight"],
}

# Preprocessing function
def preprocess_image(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Prediction function
def predict_image(image, crop_type):
    # Load the selected model
    model_path = model_paths.get(crop_type)
    if not model_path:
        return "Invalid crop type selected."

    model = tf.keras.models.load_model(model_path)

    # Preprocess the image
    img_array = preprocess_image(image)

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    # Get class label
    label = class_labels[crop_type][predicted_class]
    return label, confidence

# Streamlit app
st.title("Crop Disease Prediction")
st.write("Upload an image of your crop and select the crop type to predict its health status.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
crop_type = st.selectbox("Select Crop Type", list(model_paths.keys()))

if st.button("Predict"):
    if uploaded_file is not None and crop_type:
        # Save the uploaded file temporarily
        temp_file_path = os.path.join("temp", uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Predict the disease
        label, confidence = predict_image(temp_file_path, crop_type)
        st.success(f"Prediction: {label} (Confidence: {confidence * 100:.2f}%)")
    else:
        st.error("Please upload an image and select a crop type.")