import json
from datetime import date

from sources import SOURCES
from filters import is_local, detect_category
from utils import get_soup, extract_first_paragraph

RESULTS = []

def scrape_source(source):
    soup = get_soup(source["url"])
    if not soup:
        return  # ❌ nicht continue, hier return

    for a in soup.select("a"):
        title = a.get_text(strip=True)
        href = a.get("href")
        if not title or not href:
            continue  # ✅ korrekt: innerhalb der Schleife

        if href.startswith("/"):
            href = source["url"].split("/")[0] + "//" + source["url"].split("/")[2] + href

        if not is_local(title):
            continue  # ✅ korrekt: innerhalb der Schleife

        summary = extract_first_paragraph(href)

        # Duplikate prüfen
        if any(r["title"] == title or r["source"]["url"] == href for r in RESULTS):
            continue  # ✅ korrekt: innerhalb der Schleife

        # Qualitätsfilter
        if len(summary.strip()) < 50 or "." not in summary:
            continue  # ✅ korrekt: innerhalb der Schleife

        # Kategorie
        category_hint = source.get("category_hint")
        category = category_hint if category_hint else detect_category(title + " " + summary)

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

