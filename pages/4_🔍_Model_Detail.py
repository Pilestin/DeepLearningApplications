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
    