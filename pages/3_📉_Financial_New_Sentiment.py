import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os 


current_path = os.getcwd()
saved_models_path = "C:/Users/Yasin/Desktop/saved_models"

st.write(saved_models_path)
max_len = 50
vocab_size = 10000
labels = ['Negative', 'Neutral', 'Positive']

# Model ve tokenizer yükle
@st.cache_resource
def load_resources():
    model = load_model(os.path.join(saved_models_path, 'lstm_model.h5'))
    with open('tokenizer/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_resources()

# Streamlit Arayüzü
st.title("🧠 Finans Haberleri Duygu Analizi")
st.markdown("Bir haber başlığı veya içeriği girin. Model olumlu, olumsuz veya nötr olup olmadığını tahmin etsin.")

user_input = st.text_area("📄 Haber Metni:", height=150)

if st.button("Tahmin Et"):
    if user_input.strip() == "":
        st.warning("Lütfen bir haber metni girin.")
    else:
        # Metni vektörleştir
        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=max_len, padding='post')
        
        # Tahmin yap
        prediction = model.predict(padded)
        class_index = np.argmax(prediction)
        sentiment = labels[class_index]
        confidence = float(np.max(prediction)) * 100

        st.success(f"📈 Tahmin: **{sentiment}** ({confidence:.2f}% güven)")
