import streamlit as st
import numpy as np
from PIL import Image
import random

st.title("🍎 Klasifikasi Buah (FRESH OR ROTTEN")

file = st.file_uploader("Upload gambar", type=["jpg","jpeg","png"])

# label contoh (sesuaikan kalau mau)
classes = [
    "fresh_apple",
    "rotten_apple",
    "fresh_banana",
    "rotten_banana",
    "fresh_orange",
    "rotten_orange"
]

if file:
    img = Image.open(file).convert("RGB")
    st.image(img, caption="Gambar yang diupload")

    # "prediksi dummy"
    pred = random.choice(classes)

    st.success(f"Hasil Prediksi: {pred}")