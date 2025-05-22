import streamlit as st
from transformers import pipeline
import time

# Model yükleme (bir defa cache'lenir)
@st.cache_resource
def load_summarizer():
    # Türkçe için optimize edilmiş model
    # "ozcangundes/mt5-small-turkish-summarization" gibi Türkçe özetleme için eğitilmiş bir model 
    summarizer = pipeline(
        "summarization", 
        model="ozcangundes/mt5-small-turkish-summarization",
        device=0 if "cuda" in str(st.__version__) else -1  # GPU kullanın (varsa)
    )
    return summarizer

with st.spinner("Model yükleniyor... (ilk çalıştırmada biraz zaman alabilir)"):
    summarizer = load_summarizer()

st.title("🗞️ Metin Özetleyici - Türkçe")

default_text = """
ChatGPT, OpenAI tarafından geliştirilen bir dil modelidir ve birçok sektörde kullanılmaya başlanmıştır. Eğitimden sağlığa,
müşteri hizmetlerinden yazılım geliştirmeye kadar farklı alanlarda yapay zeka destekli çözümler sunulmaktadır.
Bu gelişmeler, insanların iş yapma şeklini değiştirmekte ve üretkenliği artırmaktadır.
"""



text = st.text_area("📌 Metin Metnini Girin:", default_text, height=200)

with st.sidebar:
    st.subheader("Özetleme Ayarları")
    max_length = st.slider("Maksimum uzunluk", 30, 150, 60)
    min_length = st.slider("Minimum uzunluk", 10, 50, 20)
    
    st.subheader("İleri Düzey Ayarlar")
    show_advanced = st.checkbox("İleri düzey ayarları göster", False)
    
    if show_advanced:
        num_beams = st.slider("Beam sayısı", 1, 8, 4)
        no_repeat_ngram_size = st.slider("Tekrarlama önleme (n-gram)", 1, 4, 2)
    else:
        num_beams = 4
        no_repeat_ngram_size = 2

if st.button("🧠 Özetle"):
    if len(text.strip()) == 0:
        st.warning("Lütfen özetlenecek bir metin girin.")
    else:
        start_time = time.time()
        
        with st.spinner("Metin özetleniyor..."):
            try:
                summary = summarizer(
                    text, 
                    max_length=max_length, 
                    min_length=min_length,
                    num_beams=num_beams, 
                    no_repeat_ngram_size=no_repeat_ngram_size,
                    early_stopping=True
                )[0]['summary_text']
                
                # process üsresi
                process_time = time.time() - start_time
                
                st.subheader("📄 Özet:")
                st.success(summary)
                st.info(f"Özetleme süresi: {process_time:.2f} saniye")
                
                # Karakter sayıları gösterimi
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Orijinal metin", f"{len(text)} karakter")
                with col2:
                    st.metric("Özet", f"{len(summary)} karakter", 
                              f"-%{int((1 - len(summary)/len(text)) * 100)}")
                              
            except Exception as e:
                st.error(f"Özetleme sırasında bir hata oluştu: {str(e)}")