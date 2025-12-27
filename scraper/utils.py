import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "MainTauberNewsBot/1.0"
}

def get_soup(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            print(f"Skipping URL (status {r.status_code}): {url}")
            return None
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_first_paragraph(url, max_len=300):
    soup = get_soup(url)
    if not soup:
        return ""
    p = soup.find("p")
    if not p:
        return ""
    return p.get_text(strip=True)[:max_len]
