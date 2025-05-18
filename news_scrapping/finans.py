import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime

def finans_news(base_url: str = "https://www.doviz.com", limit: int = 5) -> List[Dict]:
    """
    Finans haberlerini çeker ve işler.
    
    Args:
        base_url (str): Haber kaynağının URL'i
        limit (int): Çekilecek maksimum haber sayısı
        
    Returns:
        List[Dict]: Haberlerin listesi. Her haber bir sözlük olarak:
            - title: Haber başlığı
            - summary: Haber özeti
            - content: Haber içeriği
            - time: Haber zamanı
            - link: Haber linki
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    news_list = []
    
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        news_items = soup.select("div.news-list > a")[:limit]
        
        for item in news_items:
            news_data = {}
            
            title_tag = item.select_one(".headline-default")
            summary_tag = item.select_one(".summary")
            time_tag = item.select_one(".timestamp")
            thumbnail_tag = item.select_one("img")
            
            news_data["title"] = title_tag.get_text(strip=True) if title_tag else ""
            news_data["summary"] = summary_tag.get_text(strip=True) if summary_tag else ""
            news_data["time"] = time_tag.get_text(strip=True) if time_tag else ""
            news_data["image"] = thumbnail_tag["src"] if thumbnail_tag else ""
            news_data["link"] = item.get("href")
            
            # Haber detayını çek
            try:
                detail_response = requests.get(news_data["link"], headers=headers)
                detail_response.raise_for_status()
                detail_soup = BeautifulSoup(detail_response.text, "html.parser")
                
                content_div = detail_soup.find("div", class_="content")
                if content_div:
                    paragraphs = content_div.find_all("p")
                    news_data["content"] = "\n".join(p.get_text(strip=True) 
                                                   for p in paragraphs 
                                                   if p.get_text(strip=True))
                else:
                    news_data["content"] = ""
                    
            except requests.RequestException:
                news_data["content"] = "İçerik çekilemedi"
            
            news_list.append(news_data)
            
    except requests.RequestException as e:
        print(f"Hata oluştu: {e}")
        return []
        
    return news_list

def format_news(news_list: List[Dict]) -> None:
    """
    Haberleri formatli şekilde ekrana yazdırır.
    
    Args:
        news_list (List[Dict]): finans_news fonksiyonundan dönen haber listesi
    """
    for news in news_list:
        print(f"Başlık: {news['title']}")
        print(f"Özet: {news['summary']}")
        print(f"Zaman: {news['time']}")
        print(f"İçerik: {news['content']}")  # İlk 200 karakter
        print(f"Link: {news['link']}")
        print("=" * 100)
