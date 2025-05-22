# AI Bot - Türkçe Metin Özetleme VE Finans Sentiment Analiz 

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

## Test Etmek için Örnek Veriler

### Örnek Özetleme Metni
```text
Xiaomi, uzun zamandır gündemde olan elektrikli SUV modeli YU7'yi resmen tanıttı. Piyasadaki tüm SUV'lara kafa tutan otomobil, tasarımıyla da özellikleriyle de tüketicileri mest etmeyi başaracak gibi görünüyor.
Bir süre önce elektrikli otomobil pazarına iddialı bir giriş yapan Çinli teknoloji devi Xiaomi, bugün düzenlediği bir etkinlikte "YU7" olarak isimlendirdiği yeni otomobilini tanıttı. Bir SUV olarak karşımıza çıkan Xiaomi YU7, tasarımıyla da özellikleriyle de tüm dikkatleri üzerine çekmeyi başaracak gibi görünüyor. Gelin hep birlikte Xiaomi YU7 ile ilgili tüm detaylara yakından bakalım.

Oldukça şık bir tasarıma sahip olan Xiaomi YU7, markanın ilk otomobili olan SU7'yi andırıyor. Hemen hemen aynı LED destekli far tasarımının kullanıldığı YU7, arka kısımda da oldukça şık bir ışık barına ev sahipliği yapıyor. 5 metre uzunluğunda, 1,6 metre yüksekliğinde ve 2 metre genişliğinde olan otomobil, bu ölçüleriyle yollarda oldukça gösterişli bir SUV olarak yer alacak. Ancak Xiaomi YU7, bu iri boyutlarına rağmen oldukça aerodinamik bir otomobil. Açıklanan sürtünme katsayısı 0,245. 

### 📈 Positive (Olumlu) Metinler:

1. **Positive** — "Apple shares surged 5% after the company reported record quarterly earnings driven by strong iPhone sales."
2. **Positive** — "Tesla's stock rallied as the company announced expansion into the Indian market with promising government support."
3. **Positive** — "Microsoft exceeded analyst expectations with better-than-expected revenue growth across all segments."
4. **Positive** — "The central bank signaled rate cuts, which boosted investor confidence and led to a market-wide rally."
5. **Positive** — "Amazon announced a stock buyback plan worth $10 billion, boosting investor sentiment."

---

### 📉 Negative (Olumsuz) Metinler:

1. **Negative** — "Google's parent company Alphabet missed its earnings target, causing its stock to drop over 7%."
2. **Negative** — "The Fed raised interest rates by 0.5%, leading to widespread declines across tech stocks."
3. **Negative** — "Intel issued a profit warning citing weak demand in the PC market, dragging down semiconductor stocks."
4. **Negative** — "Bank of America faced regulatory fines related to compliance failures, pushing shares down by 4%."
5. **Negative** — "China's manufacturing slowdown fueled fears of a global economic recession, sending markets into a downward spiral."

---

### ⚖️ Neutral (Tarafsız) Metinler:

1. **Neutral** — "The S&P 500 closed slightly lower on Tuesday following mixed economic data."
2. **Neutral** — "Meta Platforms will host its annual developer conference next month to unveil new product features."
3. **Neutral** — "Gold prices remained flat as investors awaited inflation data and central bank decisions."
4. **Neutral** — "Netflix maintained its market position with steady user growth in line with forecasts."
5. **Neutral** — "The Nasdaq traded sideways as investors digested quarterly earnings reports from major firms."


## Teşekkür

Bu projenin geliştirilmesinde Hugging Face platformunda bulunan aşağıda linki verilen model kullanılmıştır. Bu model, Türkçe metin özetleme için özel olarak eğitilmiştir ve yüksek performans göstermektedir. Geliştiricilere katkılarından dolayı teşekkür ederim.

Model Linki: [mt5-small-turkish-summarization](https://huggingface.co/ozcangundes/mt5-small-turkish-summarization)
