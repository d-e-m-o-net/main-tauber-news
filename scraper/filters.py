PLACES = [
    "main-tauber", "bad mergentheim", "wertheim",
    "tauberbischofsheim", "lauda", "königshofen",
    "boxberg", "külsheim", "weikersheim",
    "assamstadt", "igersheim", "niederstetten",
    "creglingen", "großrinderfeld"
]

CATEGORIES = {
    "Blaulicht": ["polizei", "feuerwehr", "unfall", "brand"],
    "Kriminalität": ["straftat", "ermittlung", "gericht"],
    "Sport": ["spiel", "sieg", "liga", "meister"],
    "Politik": ["gemeinderat", "kreistag", "bürgermeister"],
    "Kultur": ["konzert", "fest", "theater"],
    "Verein": ["verein", "ehrenamt"],
    "Schule": ["schule", "schüler"],
    "Wirtschaft": ["unternehmen", "betrieb"],
    "Umwelt": ["klima", "energie", "naturschutz"]
}

def is_local(text):
    t = text.lower()
    return any(p in t for p in PLACES)

def detect_category(text):
    t = text.lower()
    for cat, words in CATEGORIES.items():
        if any(w in t for w in words):
            return cat
    return "Sonstiges"

