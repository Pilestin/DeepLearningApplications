import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import os
from datetime import datetime
from urllib.parse import urlparse
import hashlib

from static.css import css_string
from news_scrapping.finans import finans_news
from news_scrapping.teknoloji import teknoloji_news


# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Haber Özetleyici",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS ekleme
st.markdown(css_string, unsafe_allow_html=True)

# Veri depolama için dizin oluşturma
DATA_DIR = "news_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Oturum durumu yönetimi
if 'news_data' not in st.session_state:
    st.session_state.news_data = []
if 'summarized_news' not in st.session_state:
    st.session_state.summarized_news = {}
if 'all_summarized' not in st.session_state:
    st.session_state.all_summarized = False
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Teknoloji"

# Kategori tanımları
CATEGORIES = {
    "Teknoloji": {
        "url": "https://shiftdelete.net",
        "selector": "custom"  # Özel işleyici için işaret
    },
    "Gündem": {
        "url": "https://www.hurriyet.com.tr/gundem/",
        "selector": "div.container div.news-card"
    },
    "Finans": {
        "url": "https://www.doviz.com",
        "selector": "custom"  # Özel işleyici için işaret
    }
}

# Model yükleme (bir defa cache'lenir)
@st.cache_resource
def load_summarizer():
    summarizer = pipeline(
        "summarization", 
        model="ozcangundes/mt5-small-turkish-summarization",
        device=0 if "cuda" in str(st.__version__) else -1
    )
    return summarizer

# Haber metni çekme fonksiyonu
def fetch_news_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            st.write(soup.text)
            if "hurriyet.com.tr" in url:
                article_body = soup.select_one("div.news-content")
                if article_body:
                    paragraphs = article_body.find_all('p')
                    content = ' '.join([p.text for p in paragraphs])
                    return content
            else:
                # Paragraph etiketlerindeki metinleri al
                paragraphs = soup.find_all('p')
                content = ' '.join([p.text for p in paragraphs if len(p.text) > 100])
                return content
        return "İçerik çekilemedi."
    except Exception as e:
        return f"Hata: {str(e)}"

# Haber listesi çekme fonksiyonu
def fetch_news_list(category):
    news_list = []
    
    try:
        cat_info = CATEGORIES[category]
        
        # Teknoloji kategorisi için özel işleme
        if category == "Teknoloji":
            return [
                {
                    "id": hashlib.md5(news["link"].encode()).hexdigest(),
                    "title": news["title"],
                    "url": news["link"],
                    "image": news["image"],
                    "summary": news["summary"],
                    "source": "ShiftDelete.Net",
                    "date": news["time"],
                    "category": category,
                    "content": news["content"],
                    "ai_summary": None
                }
                for news in teknoloji_news(cat_info["url"], limit=10)
            ]
        
        # Finans kategorisi için özel işleme
        if category == "Finans":
            return [
                {
                    "id": hashlib.md5(news["link"].encode()).hexdigest(),
                    "title": news["title"],
                    "url": news["link"],
                    "image": news["image"],
                    "summary": news["summary"],
                    "source": "Doviz.com",
                    "date": news["time"],
                    "category": category,
                    "content": news["content"],
                    "ai_summary": None
                }
                for news in finans_news(cat_info["url"], limit=10)
            ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        st.write(f"Veri çekiliyor: {cat_info['url']}")
        response = requests.get(cat_info["url"], headers=headers, timeout=10)
        if response.status_code != 200:
            st.error(f"Veri çekilirken hata oluştu: {response.status_code}")
        else:
            st.success(f"STATUS[{response.status_code}]")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                news_items = soup.select(cat_info["selector"])
                
                for item in news_items[:10]:  
                    st.write(f"İşleniyor: {item}")
                    try:
                        title_element = item.select_one("div.news-title a, h3.news-title a")
                        if not title_element:
                            continue
                            
                        title = title_element.text.strip()
                        url = title_element['href']
                        
                        # Eğer URL tam değilse (bağıl yol), tam URL'ye dönüştür
                        if not url.startswith('http'):
                            parsed_base = urlparse(cat_info["url"])
                            base_url = f"{parsed_base.scheme}://{parsed_base.netloc}"
                            url = base_url + url
                        
                        # Resim bulma
                        img_element = item.select_one("img")
                        img_url = img_element['src'] if img_element and 'src' in img_element.attrs else ""
                        
                        # Eğer resim URL'si tam değilse (bağıl yol), tam URL'ye dönüştür
                        if img_url and not img_url.startswith('http'):
                            parsed_base = urlparse(cat_info["url"])
                            base_url = f"{parsed_base.scheme}://{parsed_base.netloc}"
                            img_url = base_url + img_url
                        
                        # Özet bulma
                        summary_element = item.select_one("div.news-summary, div.news-description")
                        summary = summary_element.text.strip() if summary_element else ""
                        
                        # Kaynak ve tarih tanımlama
                        source = "Hürriyet"
                        date = datetime.now().strftime("%d.%m.%Y")
                        
                        # Haberi benzersiz tanımlamak için hash oluşturma
                        news_id = hashlib.md5(url.encode()).hexdigest()
                        
                        news_list.append({
                            "id": news_id,
                            "title": title,
                            "url": url,
                            "image": img_url,
                            "summary": summary,
                            "source": source,
                            "date": date,
                            "category": category,
                            "content": None,  # İçerik sonradan çekilecek
                            "ai_summary": None  # AI özeti sonradan oluşturulacak
                        })
                    except Exception as e:
                        continue
        
        return news_list
    except Exception as e:
        st.error(f"Haberler çekilirken hata oluştu: {str(e)}")
        return []

# Haber özetleme fonksiyonu
def summarize_news(content, max_length=350, min_length=50):
    if not content or len(content.strip()) < 100:
        return "Özetlenecek yeterli içerik bulunamadı."
    
    try:
        # İçeriği temizle ve düzenle
        cleaned_content = clean_content(content)
        
        # Çok uzun metinleri parçalara böl
        if len(cleaned_content) > 1024:
            parts = split_content(cleaned_content)
            summaries = []
            
            for part in parts:
                summarizer = load_summarizer()
                summary = summarizer(
                    part, 
                    max_length=max_length // len(parts), 
                    min_length=min_length,
                    num_beams=4, 
                    no_repeat_ngram_size=2,
                    early_stopping=True,
                    do_sample=True,  # Çeşitlilik için
                    top_k=50,        # En iyi 50 tokeni kullan
                    top_p=0.95       # Olasılık eşiği
                )[0]['summary_text']
                summaries.append(summary)
            
            # Parça özetlerini birleştir
            final_summary = " ".join(summaries)
            
            # Son bir kez daha özetle
            final_summary = summarizer(
                final_summary,
                max_length=max_length,
                min_length=min_length,
                num_beams=4,
                no_repeat_ngram_size=2,
                early_stopping=True
            )[0]['summary_text']
            
            return final_summary
        else:
            summarizer = load_summarizer()
            return summarizer(
                cleaned_content,
                max_length=max_length,
                min_length=min_length,
                num_beams=4,
                no_repeat_ngram_size=2,
                early_stopping=True,
                do_sample=True,
                top_k=50,
                top_p=0.95
            )[0]['summary_text']
            
    except Exception as e:
        return f"Özetleme sırasında hata: {str(e)}"

def clean_content(content: str) -> str:
    """İçeriği temizler ve düzenler."""
    import re
    
    # Gereksiz boşlukları temizle
    content = ' '.join(content.split())
    
    # URL'leri kaldır
    content = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', content)
    
    # Özel karakterleri temizle
    content = re.sub(r'[^\w\s\.,!?]', '', content)
    
    # Çoklu noktalama işaretlerini tekli yap
    content = re.sub(r'\.+', '.', content)
    content = re.sub(r'\!+', '!', content)
    content = re.sub(r'\?+', '?', content)
    
    return content.strip()

def split_content(content: str, max_length: int = 1024) -> list:
    """Uzun içeriği anlamlı parçalara böler."""
    # Cümlelere böl
    sentences = content.split('.')
    parts = []
    current_part = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip() + '.'
        if current_length + len(sentence) > max_length:
            if current_part:
                parts.append(' '.join(current_part))
            current_part = [sentence]
            current_length = len(sentence)
        else:
            current_part.append(sentence)
            current_length += len(sentence)
    
    if current_part:
        parts.append(' '.join(current_part))
    
    return parts

# Haberi özetleme ve session state'e kaydetme
def summarize_and_save(news_id):
    for i, news in enumerate(st.session_state.news_data):
        if news["id"] == news_id:
            if not news["content"]:
                with st.spinner(f"'{news['title']}' haberi çekiliyor..."):
                    content = fetch_news_content(news["url"])
                    if len(content.strip()) < 100:
                        content = news["summary"]  # Eğer içerik çekilemediyse özeti kullan
                    news["content"] = content
                    st.session_state.news_data[i] = news
            
            if news["content"]:
                with st.spinner(f"'{news['title']}' haberi özetleniyor..."):
                    summary = summarize_news(
                        news["content"],
                        max_length=350,  
                        min_length=100   
                    )
                    news["ai_summary"] = summary
                    st.session_state.news_data[i] = news
                    st.session_state.summarized_news[news_id] = True
            break
    
    st.rerun()

# Tüm haberleri özetleme
def summarize_all_news():
    with st.spinner("Tüm haberler özetleniyor..."):
        progress_bar = st.progress(0)
        total_news = len(st.session_state.news_data)
        
        for i, news in enumerate(st.session_state.news_data):
            # İçerik henüz çekilmemişse çek
            if not news["content"]:
                news["content"] = fetch_news_content(news["url"])
            
            # İçerik varsa özetle
            if news["content"]:
                summary = summarize_news(news["content"])
                news["ai_summary"] = summary
                st.session_state.summarized_news[news["id"]] = True
            
            # İlerleme güncellemesi
            progress_bar.progress((i + 1) / total_news)
        
        st.session_state.all_summarized = True
    
    st.rerun()

# Kategori değiştirme fonksiyonu
def change_category(category):
    if st.session_state.selected_category != category:
        st.session_state.selected_category = category
        st.session_state.news_data = []
        st.session_state.summarized_news = {}
        st.session_state.all_summarized = False
        
        with st.spinner(f"{category} haberleri yükleniyor..."):
            st.session_state.news_data = fetch_news_list(category)

    st.rerun()

# Ana uygulama fonksiyo
def main():

    st.markdown("<div class='app-header'><h1>📰 Haber Özetleyici</h1></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='category-selector'>", unsafe_allow_html=True)
    cols = st.columns(len(CATEGORIES))
    for i, category in enumerate(CATEGORIES.keys()):
        with cols[i]:
            if st.button(
                category, 
                key=f"cat_{category}", 
                use_container_width=True,
                type="primary" if st.session_state.selected_category == category else "secondary"
            ):
                change_category(category)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown(f"<h2>📌 {st.session_state.selected_category} Haberleri</h2>", unsafe_allow_html=True)
    
    if not st.session_state.news_data:
        with st.spinner(f"{st.session_state.selected_category} haberleri yükleniyor..."):
            st.session_state.news_data = fetch_news_list(st.session_state.selected_category)
    
    if st.button("🧠 Tüm Haberleri Özetle", type="primary"):
        summarize_all_news()
    
    if st.session_state.all_summarized:
        st.markdown("<div class='summary-header'><h2>📋 Tüm Haberler - Özet</h2></div>", unsafe_allow_html=True)
        
        for i, news in enumerate(st.session_state.news_data):
            if news["ai_summary"]:
                st.markdown(f"""
                <div class='summary-item'>
                    <strong>{i+1}. {news['title']}</strong><br>
                    {news['ai_summary']}
                </div>
                """, unsafe_allow_html=True)
    
    if st.session_state.news_data:
        cols_per_row = 3
        for i in range(0, len(st.session_state.news_data), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                idx = i + j
                if idx < len(st.session_state.news_data):
                    news = st.session_state.news_data[idx]
                    with cols[j]:
                        st.markdown(f"""
                        <div class='news-card'>
                            <img src="{news['image'] if news['image'] else 'https://via.placeholder.com/300x200'}" class='news-image'>
                            <div class='news-title'>{news['title']}</div>
                            <div class='news-source'>{news['image']}</div>
                            <div class='news-source'>{news['source']}</div>
                            <div class='news-date'>{news['date']}</div>
                            <div class='news-summary'>{news['summary']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"<a href='{news['url']}' target='_blank'><button style='width:100%;'>Habere Git</button></a>", unsafe_allow_html=True)
                        with col2:
                            if news["id"] in st.session_state.summarized_news:
                                if st.button("Özeti Göster", key=f"show_{news['id']}"):
                                    st.info(news["ai_summary"])
                            else:
                                if st.button("Özetle", key=f"sum_{news['id']}"):
                                    summarize_and_save(news["id"])
    else:
        st.info(f"Henüz {st.session_state.selected_category} kategorisinde haber bulunamadı.")

if __name__ == "__main__":
    main()
