import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

st.title("Jackfruit Leaf Disease Classifier 🌿")

# Image upload
uploaded_file = st.file_uploader("পাতার ছবি আপলোড করুন:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    # Model load (saved model path)
    model = tf.keras.models.load_model("leaf_model.h5")

    # Preprocess image
    img = image.resize((224, 224))   # model input size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    result = np.argmax(prediction)

    if result == 0:
        st.success("✅ Healthy Leaf")
    else:
        st.error("⚠️ Diseased Leaf")

