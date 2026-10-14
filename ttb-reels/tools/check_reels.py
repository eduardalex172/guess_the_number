"""Validate TTB reel specs: required fields, estimated length, and the copy rules from PLAN.md (14 Oct)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WPS = 2.6  # Brian v4 at speed 1.05, measured roughly from r02-inanna (50.5 s)
PAD, TAIL, LEAD = 0.25, 2.2, 0.3
STYLES = {f"S{i}" for i in range(1, 11)}
STATUSES = {"KNOWN", "DEBATED", "SPECULATION"}
GRADES = {"warm", "orange", "red", "magenta", "teal", "mono", "cool"}
# TTB rejected "stock actors acting": shots show places, objects, archive, line art, never people performing.
ACTORS = re.compile(r"\b(man|woman|person|people|actor|girl|boy|family|couple|someone)\b", re.I)
BANNED = [
    r"\bsource:", r"watch (the )?full", r"on youtube", r"link in bio", r"full story",
    r"which .* would you choose", r"comment below", r"let me know in the comments", r"smash",
]


def est_seconds(reel):
    words = sum(len(l["say"].split()) for l in reel["lines"])
    return LEAD + words / WPS + PAD * len(reel["lines"]) + TAIL, words


def check(reel):
    errs = []
    for k in ("id", "pillar", "sub", "style", "status", "hook", "lines", "ig_caption", "tt_caption", "fact_note"):
        if not reel.get(k):
            errs.append(f"missing {k}")
    if reel.get("style") not in STYLES:
        errs.append(f"bad style {reel.get('style')}")
    if reel.get("status") not in STATUSES:
        errs.append(f"bad status {reel.get('status')}")
    seen = set()
    lines = reel.get("lines", [])
    if not 6 <= len(lines) <= 10:
        errs.append(f"{len(lines)} lines (want 6-10)")
    for i, l in enumerate(lines):
        if not l.get("say") or not l.get("shots"):
            errs.append(f"line {i} needs say + shots")
            continue
        if not 2 <= len(l["shots"]) <= 3:
            errs.append(f"line {i} has {len(l['shots'])} shots (want 2-3)")
        for shot in l["shots"]:
            desc, grade = shot[0], shot[1]
            if grade not in GRADES:
                errs.append(f"line {i} bad grade {grade}")
            if desc in seen:
                errs.append(f"repeated shot: {desc}")
            seen.add(desc)
            if ACTORS.search(desc) and not re.search(r"\b(bust|statue|portrait|photo|painting|engraving|line art|archive|AI art)", desc, re.I):
                errs.append(f"stock actor? {desc}")
    secs, words = est_seconds(reel)
    if not 35 <= secs <= 62:
        errs.append(f"length {secs:.0f}s ({words} words) outside 35-60s")
    for field in ("ig_caption", "tt_caption", "outro"):
        text = reel.get(field, "") or ""
        for pat in BANNED:
            if re.search(pat, text, re.I):
                errs.append(f"{field} breaks copy rule /{pat}/")
        if text.count("#") > 3:
            errs.append(f"{field} has more than 3 hashtags")
    for l in reel.get("lines", []):
        for pat in BANNED[1:5]:
            if re.search(pat, l["say"], re.I):
                errs.append(f"narration sends viewers away /{pat}/")
    return errs, secs


def main():
    ids, bad, total = set(), 0, 0
    styles = {}
    for f in sorted((ROOT / "reels").glob("P*.json")):
        for reel in json.loads(f.read_text(encoding="utf-8")):
            total += 1
            errs, secs = check(reel)
            if reel["id"] in ids:
                errs.append("duplicate id")
            ids.add(reel["id"])
            styles[reel["style"]] = styles.get(reel["style"], 0) + 1
            if errs:
                bad += 1
                print(f"{f.name} {reel['id']}: " + "; ".join(errs))
    print(f"{total} reels, {bad} with problems. Styles: " + ", ".join(f"{k}={v}" for k, v in sorted(styles.items(), key=lambda x: int(x[0][1:]))))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
