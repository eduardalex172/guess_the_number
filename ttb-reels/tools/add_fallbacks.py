"""Append a generic Envato fallback (' || alt: ...') to 'q:' shots that name a specific site, object or place.

TTB tip (14 Oct): exact archaeological sites are often missing from Envato, so each specific query
carries a second, generic search term. Idempotent: shots that already have '|| alt:' are skipped.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# specific name -> generic stand-in (longest names are matched first)
GENERIC = {
    "Gobekli Tepe T-shaped": "megalithic T-shaped", "Gobekli Tepe": "ancient megalithic stone ruins",
    "Great Pyramid of Giza": "Egyptian pyramid", "Giza": "Egyptian desert pyramids", "Stonehenge": "stone circle",
    "Antikythera": "Greek island", "Athens Acropolis": "ancient Greek temple hill", "Parthenon Athens": "Greek temple",
    "Parthenon": "Greek temple", "Pantheon Rome": "Roman domed temple", "Pantheon": "Roman dome",
    "Olympia": "ancient Greek", "Karnak": "Egyptian temple", "Amarna": "desert", "Abydos": "Egyptian temple",
    "Osireion": "ancient flooded temple", "Qumran": "desert cliff", "Dead Sea": "desert salt lake",
    "Nineveh": "ancient Near East", "Mosul": "Middle East city", "Babylon": "ancient Mesopotamian",
    "Ishtar": "ancient blue tiled", "Ur": "Mesopotamian", "Euphrates": "desert river", "Mesopotamian": "desert river",
    "Karacadag": "barren hills", "Hagia Sophia": "Byzantine church", "Istanbul": "old city", "Bosphorus": "strait",
    "Byblos Lebanon": "Mediterranean ancient", "Mount Lebanon": "Mediterranean mountain", "Lebanese": "Mediterranean",
    "Golan": "dry highland", "Bejaia Algeria": "North African", "Upper Egypt": "desert river valley",
    "Red Sea": "desert", "Varanasi": "Indian river city", "Jantar Mantar": "historic stone observatory",
    "Jaipur": "Indian", "Potala Palace Lhasa": "Himalayan palace", "Amdo": "high plateau",
    "Tikal": "jungle pyramid", "Malta Hypogeum": "underground carved rock chamber", "Malta": "Mediterranean",
    "Ostia": "Roman", "Vesuvius": "volcano", "Prague": "medieval", "Florence": "old Italian city",
    "Pisa": "old Italian", "Zurich": "old European city", "Danube": "wide European river",
    "Cork Ireland": "old European", "Newfoundland": "rugged north Atlantic", "Norfolk": "rural English",
    "Oxford University": "old university", "Princeton University": "old university", "Princeton": "old university",
    "University of Virginia": "old American university", "Cambridge": "old university",
    "Paris Institut": "historic domed", "Hotel New Yorker": "vintage hotel", "Lower Manhattan": "old city",
    "Long Island": "coastline", "Puget Sound": "coastal bay", "Phoenix Arizona": "desert city",
    "New Mexico": "American desert", "Louisiana": "swamp", "Vermont": "rural hills", "Chicago": "American city",
    "Colorado": "American mountain town", "Atlantic City": "seaside", "Washington DC": "capital",
    "Chile Andes": "mountain", "Sri Lanka": "tropical", "Blue Ridge": "forested mountains",
    "Indonesia": "tropical", "Hollywood": "city", "LIGO": "large physics laboratory", "NIST": "physics lab",
    "Hubble": "space telescope", "Bootes": "star field", "Andromeda": "spiral galaxy", "Orion": "constellation",
    "Big Dipper": "constellation", "Uranus Neptune": "outer planets", "Saturn": "ringed planet",
    "Calabi-Yau": "abstract folded geometry", "Tutankhamun": "gold Egyptian", "Chladni": "vibrating plate",
}
NAMES = sorted(GENERIC, key=len, reverse=True)


def fallback(desc):
    q = desc[3:].strip()
    hit = False
    for name in NAMES:
        pat = rf"\b{re.escape(name)}\b"
        if re.search(pat, q):
            q = re.sub(pat, GENERIC[name], q)
            hit = True
    # 'Egyptian temple temple columns' -> 'Egyptian temple columns'
    q = re.sub(r"\b(\w+)(\s+\1\b)+", r"\1", q, flags=re.I)
    return q if hit else None


def main():
    added = 0
    for f in sorted((ROOT / "reels").glob("P*.json")):
        reels = json.loads(f.read_text(encoding="utf-8"))
        for r in reels:
            for l in r["lines"]:
                for s in l["shots"]:
                    if s[0].startswith("q:") and "|| alt:" not in s[0]:
                        alt = fallback(s[0])
                        if alt:
                            s[0] = f"{s[0]} || alt: {alt}"
                            added += 1
        f.write_text(json.dumps(reels, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added {added} fallbacks")


if __name__ == "__main__":
    main()
