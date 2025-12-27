import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "MainTauberNewsBot/1.0"
}

def get_soup(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def extract_first_paragraph(url, max_len=300):
    try:
        soup = get_soup(url)
        p = soup.find("p")
        if not p:
            return ""
        return p.get_text(strip=True)[:max_len]
    except Exception:
        return ""

