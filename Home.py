import streamlit as st

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Ana Sayfa",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stilleri
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        background: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .card-title {
        color: #1e3c72;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .card-text {
        color: #666;
        font-size: 1rem;
    }
    .emoji-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        color: #666;
        position: fixed;
        bottom: 0;
        width: 100%;
        background: white;
    }
    .stButton {
        width: 100%;
    }
    /* Kartlar arasındaki boşluğu ayarla */
    .card {
        margin: 0.5rem;
        min-height: 250px;
    }
    /* Responsive tasarım için */
    @media screen and (max-width: 768px) {
        .card {
            margin: 1rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown("<div class='main-header'><h1>🤖 Metin İşleme Asistanı</h1></div>", unsafe_allow_html=True)

# Kısa açıklama
st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <p>Yapay zeka destekli metin işleme ve haber özetleme araçları</p>
    </div>
""", unsafe_allow_html=True)

# Sayfalar için kartlar
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class='card'>
            <div class='emoji-icon'>𓂃🖊</div>
            <div class='card-title'>Metin Özetleyici</div>
            <div class='card-text'>
                Metin özetleme aracı, Türkçe metinleri özetleyerek kısa ve öz hale getirir.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Özetleyiciye Git", key="btn1"):
        st.switch_page("pages/1_𓂃🖊_Summarizer.py")

with col2:
    st.markdown("""
        <div class='card'>
            <div class='emoji-icon'>📰</div>
            <div class='card-title'>Haber Özetleyici</div>
            <div class='card-text'>
                Farklı kategorilerde güncel haberleri otomatik olarak çekin ve özetleyin.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Haberlere Git", key="btn2"):
        st.switch_page("pages/2_📰_News.py")

with col3:
    st.markdown("""
        <div class='card'>
            <div class='emoji-icon'>📉</div>
            <div class='card-title'>Finans Duygu Analizi</div>
            <div class='card-text'>
                Finans haberlerinin duygusal tonunu analiz edin ve piyasa etkisini değerlendirin.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Duygu Analizine Git", key="btn3"):
        st.switch_page("pages/3_📉_Financial_News_Sentiment.py")

with col4:
    st.markdown("""
        <div class='card'>
            <div class='emoji-icon'>🔍</div>
            <div class='card-title'>Model Detayları</div>
            <div class='card-text'>
                Kullanılan yapay zeka modellerinin teknik detayları ve performans metrikleri.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Model Detaylarına Git", key="btn4"):
        st.switch_page("pages/4_🔍_Model_Detail.py")

# Alt bilgi
st.markdown("""
    <div class='footer'>
        <p>© 2025 AI Bot | Geliştirici: Yasin Ünal</p>
    </div>
""", unsafe_allow_html=True)
