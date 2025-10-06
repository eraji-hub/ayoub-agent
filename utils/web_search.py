import requests
from bs4 import BeautifulSoup

def search_web(query, num_results=5):
    """جلب روابط البحث عبر Bing (يمكن تعديل API لاحقاً)"""
    query = query.replace(' ', '+')
    url = f"https://www.bing.com/search?q={query}&count={num_results}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [a['href'] for a in soup.find_all('a', href=True) if "http" in a['href']]
    return links[:num_results]
