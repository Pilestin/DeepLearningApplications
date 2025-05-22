import streamlit as st


with st.container():
    st.markdown("""
    **Model Adı**: ozcangundes/mt5-small-turkish-summarization  
    **Mimari**: mT5-small (Multilingual T5)  
    **Eğitim Verisi**: Türkçe haber, metin veri setleri (TRSum, BounNews, ... olabilir)  
    **Parametre Sayısı**: ~300M  
    **Özellikler**:
    - Çok dilli destek
    - Sequence-to-sequence encoder-decoder yapısı
    - Transfer learning ile fine-tune edilmiş
    """)


    st.markdown("""
                
        **Model Açıklaması**:
            Google tarafından geliştirilen **Multilingual T5 (mT5-small)** modeli, çok dilli olarak önceden eğitilmiş büyük bir dil modelidir. Bu sürüm özel olarak Türkçe haber özetleme görevine yönelik fine-tune edilmiştir.

        ---

        #### Eğitim Bilgileri:
        - **Model Mimarisi**: mT5-small (Encoder-Decoder)
        - **Parametre Sayısı**: ~300 milyon
        - **Model Boyutu**: ~1.2 GB
        - **Eğitim Süresi**: ~4 saat (Google Colab'de)
        - **Eğitim Aracı**: PyTorch Lightning ⚡
        - **Epoch**: 10  
        - **Batch Size**: 8  
        - **Learning Rate**: 1e-4  
        - **Max News Length**: 784  
        - **Max Summary Length**: 64  

        ---

        #### 🧾 Veri Seti:
        - **Kaynak**: [MLSUM - Multilingual Summarization Dataset](https://github.com/recitalAI/MLSUM)
        - **Dil**: Türkçe
        - **Veri Sayısı**: 
            - 20.000 haber → eğitim  
            - 4.000 haber → doğrulama  
        - **Açıklama**: MLSUM, haberlerle birlikte insan tarafından yazılmış özetler içeren çok dilli bir veri setidir.

        ---

        #### 🔎 Dikkat Edilmesi Gerekenler:
        - mT5 modeli yalnızca **önceden eğitilmiş (pretrained)** bir modeldir, yani üzerinde görev-özel (task-specific) eğitim yapılmadığı sürece özelleştirilmiş görevlerde **performansı düşüktür**.
        - Bu nedenle **Türkçe özetleme** görevinde kullanılabilmesi için özel olarak fine-tune edilmiştir.
        """)

    st.markdown("""[ozcangundes/mt5-small-turkish-summarization](https://huggingface.co/ozcangundes/mt5-small-turkish-summarization)""")

with st.container():
    st.markdown("""### LSTM Modeli""")
    st.markdown("""
    **Model Adı**: LSTM-based Sentiment Classifier  
    **Mimari**: LSTM (Long Short-Term Memory)  
    **Eğitim Verisi**: Finans haberleri veri seti ([Kaggle](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news))  
    **Parametre Sayısı**: ~50K  
    **Özellikler**:
    - Tek katmanlı LSTM
    - Dropout ile overfitting önleme
    - Çok sınıflı sınıflandırma (olumlu, olumsuz, nötr)
    """)

    st.markdown("""
    #### Eğitim Bilgileri:
    - **Model Mimarisi**: LSTM (Tek katmanlı)
    - **Parametre Sayısı**: ~50K
    - **Model Boyutu**: ~200 KB
    - **Eğitim Süresi**: ~
    - **Eğitim Aracı**: TensorFlow/Keras
    - **Epoch**: 50  
    - **Batch Size**: 32  
    - **Learning Rate**: 1e-3  
    - **Max Sequence Length**: 50  

    ---

    #### 🧾 Veri Seti:
    - **Kaynak**: [Sentiment Analysis for Financial News](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
    - **Dil**: İngilizce
    - **Veri Sayısı**: 
        - 3.877 haber → eğitim  
        - 969 haber → doğrulama  
    - **Açıklama**: Finans haberlerini olumlu, olumsuz veya nötr olarak etiketleyen bir veri setidir.

    ---

    #### 🔎 Dikkat Edilmesi Gerekenler:
    - LSTM modeli, uzun dizilerdeki bağımlılıkları öğrenmek için tasarlanmıştır.
    - Model, yalnızca eğitim verisindeki kelimeleri öğrenir. Eğitimde görülmeyen kelimeler için `<OOV>` (Out of Vocabulary) token'ı atanır.
    """)

    st.markdown("""[LSTM Modeli Kaynağı](https://github.com/your-repo/lstm-model)""")
