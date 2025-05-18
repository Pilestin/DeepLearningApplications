# AI Bot - Türkçe Metin Özetleme Sistemi

## Proje Hakkında
Bu proje, Eskişehir Osmangazi Üniversitesi Bilgisayar Mühendisliği Anabilim Dalı Yüksek Lisans programında "Deep Learning Applications" dersi kapsamında geliştirilmiştir. Proje, Türkçe metinler için yapay zeka destekli özetleme ve haber toplama sistemi sunmaktadır.

## Özellikler
- 📝 Metin Özetleme
  - Türkçe metinler için eğitilmiş bir model kullanılmaktadır
  - Ayarlanabilir özet uzunluğu
  
- 📰 Haber Özetleme
  - Çoklu kaynak desteği
    - Teknoloji Haberleri (ShiftDelete.net)
    - Finans Haberleri (Doviz.com)
    - Gündem Haberleri (henüz eklenmedi)
  - Otomatik haber çekme
  - Yapay zeka ile haber özetleme
  
- 🔍 Model Detayları
  - Model performans metrikleri
  - Kullanılan teknolojiler hakkında bilgi

## Teknolojik Altyapı
- **Ana Çerçeve**: Python 3
- **Web Arayüzü**: Streamlit
- **NLP Modeli**: Hugging Face Transformers
- **Özetleme Modeli**: mt5-small-turkish-summarization
- **Web Scraping**: BeautifulSoup4, Requests
- **Veri İşleme**: Pandas

## Kurulum

### Gereksinimler

Python 3.8 veya üzeri

pip (Python paket yöneticisi)

Git (Versiyon kontrol sistemi)


### Kurulum Adımları
1. Projeyi klonlayın
```bash
git clone https://github.com/Pilestin/DeepLearningApplications.git
cd DeepLearningApplications
```

2. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın
```bash
streamlit run app.py
```

## Kullanım
1. Ana sayfa üzerinden istediğiniz özelliği seçin
2. Metin özetleme için direkt metin girişi yapın
3. Haber özetleme için kategori seçin ve haberleri görüntüleyin
4. Model detayları için teknik bilgileri inceleyin

## Proje Yapısı
```
Main/
├── app.py                  # Ana uygulama
├── pages/                  # Streamlit sayfaları
│   ├── 1_𓂃🖊_Summarizer.py    # Metin özetleme
│   ├── 2_📰_News.py           # Haber özetleme
│   └── 3_🔍_Model_Detail.py   # Model detayları
├── news_scrapping/        # Haber çekme modülleri
│   ├── finans.py
│   └── teknoloji.py
├── static/               # Statik dosyalar
│   └── css.py
├── requirements.txt      # Bağımlılıklar
└── README.md            # Dokümantasyon
```

## Teşekkür

Bu projenin geliştirilmesinde Hugging Face platformunda bulunan aşağıda linki verilen model kullanılmıştır. Bu model, Türkçe metin özetleme için özel olarak eğitilmiştir ve yüksek performans göstermektedir. Geliştiricilere katkılarından dolayı teşekkür ederim.

Model Linki: [mt5-small-turkish-summarization](https://huggingface.co/ozcangundes/mt5-small-turkish-summarization)
