"""Build CATALOG.md: all reels, readable on a phone (script + captions), grouped by pillar."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_reels import est_seconds  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STYLE_NAMES = {
    "S1": "Cold Case", "S2": "One Image", "S3": "Countdown", "S4": "Myth vs Record", "S5": "Voice from the Past",
    "S6": "What If", "S7": "Case File", "S8": "Made Simple", "S9": "Scale", "S10": "The Thread",
}


def render_cell(r):
    rd = r.get("render")
    return f"✓ {rd['seconds']:.0f} s" if rd and rd.get("status") == "done" else ""


def plain(hook):
    return hook.replace("|", " ").replace("*", "")


def main():
    files = sorted((ROOT / "reels").glob("P*.json"))
    pillars = [(f, json.loads(f.read_text(encoding="utf-8"))) for f in files]
    out = ["# The Thread Beneath: 100 Reels", "",
           "Generat din `reels/*.json` cu `python3 tools/build_catalog.py`. Narațiunea și descrierile sunt în engleză (public SUA).", "",
           "Stiluri: " + " · ".join(f"**{k}** {v}" for k, v in STYLE_NAMES.items()), "",
           "| ID | Hook | Stil | Status | ~s | Randat |", "|---|---|---|---|---|---|"]
    for _, reels in pillars:
        for r in reels:
            secs, _ = est_seconds(r)
            out.append(f"| [{r['id']}](#{r['id'].lower()}) | {plain(r['hook'])} | {r['style']} {STYLE_NAMES[r['style']]} | {r['status']} | {secs:.0f} | {render_cell(r)} |")
    for _, reels in pillars:
        out += ["", f"## {reels[0]['pillar']}", ""]
        for r in reels:
            secs, words = est_seconds(r)
            out += [f"### {r['id']}", "",
                    f"**{plain(r['hook'])}** · {r['style']} {STYLE_NAMES[r['style']]} · {r['sub']} · {r['status']} · ~{secs:.0f} s ({words} words)", ""]
            out += [f"{i}. {l['say']}" for i, l in enumerate(r["lines"], 1)]
            out += ["", f"- **Instagram:** {r['ig_caption']}", f"- **TikTok:** {r['tt_caption']}",
                    f"- **Fact note (internal):** {r['fact_note']}"]
            if r.get("render"):
                rd = r["render"]
                out.append(f"- **Randat:** {rd['status']}, {rd['seconds']} s, Drive: {rd['drive']}. {rd['notes']}")
            out.append("")
    (ROOT / "CATALOG.md").write_text("\n".join(out), encoding="utf-8")
    print(f"CATALOG.md: {sum(len(r) for _, r in pillars)} reels")


if __name__ == "__main__":
    main()
