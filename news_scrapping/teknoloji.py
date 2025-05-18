import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime

def teknoloji_news(base_url: str = "https://shiftdelete.net", limit: int = 5) -> List[Dict]:
    """
    Teknoloji haberlerini çeker ve işler.
    
    Args:
        base_url (str): Haber kaynağının URL'i
        limit (int): Çekilecek maksimum haber sayısı
        
    Returns:
        List[Dict]: Haberlerin listesi. Her haber bir sözlük olarak:
            - title: Haber başlığı
            - content: Haber içeriği
            - link: Haber linki
            - image: Haber görseli URL'i
            - summary: Haber özeti (içerikten kısa bir bölüm)
            - time: Haber zamanı (varsayılan olarak şu anki zaman)
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    news_list = []
    
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        articles = soup.select("div.tdb_module_loop.td_module_wrap")[:limit]
        
        for article in articles:
            news_data = {}
            
            link_tag = article.find("a", href=True)
            title_tag = article.select_one("h3.entry-title")
            
            if not link_tag or not title_tag:
                continue
                
            news_data["title"] = title_tag.get_text(strip=True)
            news_data["link"] = link_tag["href"]
            news_data["time"] = datetime.now().strftime("%d.%m.%Y")

            
            try:
                detail_res = requests.get(news_data["link"], headers=headers)
                detail_soup = BeautifulSoup(detail_res.text, "html.parser")
                
                content_div = (
                    detail_soup.select_one("div.td-post-content") or
                    detail_soup.select_one("div.tdb-block-inner.td-fix-index") or
                    detail_soup.select_one("article.post")
                )
                
                image_tag = detail_soup.select_one("img.entry-thumb")
                if image_tag and image_tag.get("src"):
                    news_data["image"] = image_tag["src"]
                else:
                    news_data["image"] = "https://ares.shiftdelete.net/2025/03/logo-2x.png"
                
                if content_div:
                    valid_tags = content_div.find_all(["p", "h2"])
                    content_lines = [
                        tag.get_text(strip=True)
                        for tag in valid_tags
                        if tag.get_text(strip=True) and "bkz" not in tag.get_text(strip=True).lower()
                    ]
                    news_data["content"] = "\n".join(content_lines)
                    # İçeriğin ilk 200 karakterini özet olarak al
                    news_data["summary"] = news_data["content"][:200] + "..."
                else:
                    news_data["content"] = "İçerik bulunamadı"
                    news_data["summary"] = "Özet bulunamadı"
                    
            except requests.RequestException:
                news_data["content"] = "İçerik çekilemedi"
                news_data["summary"] = "Özet bulunamadı"
            
            news_list.append(news_data)
            
    except requests.RequestException as e:
        print(f"Hata oluştu: {e}")
        return []
        
    return news_list

def format_tech_news(news_list: List[Dict]) -> None:
    """
    Teknoloji haberlerini formatli şekilde ekrana yazdırır.
    
    Args:
        news_list (List[Dict]): teknoloji_news fonksiyonundan dönen haber listesi
    """
    for news in news_list:
        print(f"📰 Başlık: {news['title']}")
        print(f"🔗 Link: {news['link']}")
        print(f"📅 Tarih: {news['time']}")
        print(f"📄 Özet: {news['summary']}")
        print("=" * 100)
