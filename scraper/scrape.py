import json
from datetime import date

from sources import SOURCES
from filters import is_local, detect_category
from utils import get_soup, extract_first_paragraph

RESULTS = []

def scrape_source(source):
    soup = get_soup(source["url"])
    if not soup:
        return

    for a in soup.select("a"):
        title = a.get_text(strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        if href.startswith("/"):
            href = source["url"].split("/")[0] + "//" + source["url"].split("/")[2] + href

        if not is_local(title):
            continue

        # Wenn Kategorie "Blaulicht" vorgegeben ist, direkt übernehmen
    category_hint = source.get("category_hint")
    if category_hint:
        category = category_hint
    else:
        category = detect_category(title + " " + summary)

        summary = extract_first_paragraph(href)

        # ✅ Duplikate vermeiden
        if any(r["title"] == title or r["source"]["url"] == href for r in RESULTS):
            continue

        # ✅ Nur aufnehmen, wenn es etwas Text gibt
        if not summary.strip():
            continue        

RESULTS.append({
    "category": category,
    "title": title,
    "summary": summary,
    "source": {
        "name": source["name"],
        "url": href
    }
})

def main():
    for source in SOURCES:
        scrape_source(source)

    data = {
        "date": str(date.today()),
        "region": "Main-Tauber-Kreis",
        "items": RESULTS
    }

    with open("data/latest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()

