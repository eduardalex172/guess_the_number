"""Export chosen reels to pilot/NN-slug/reel.json (pure make-reel.mjs format) + post.txt (copy for the phone).

Shot paths are left as search descriptions ("q: ...", "archive: ...", "line art: ...");
the TTB session swaps them for real files before running make-reel.mjs.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PILOT = ["P01-01", "P04-06", "P02-05", "P05-07", "P04-07", "P02-09", "P03-01", "P04-01", "P02-10", "P01-06"]


def load_all():
    reels = {}
    for f in sorted((ROOT / "reels").glob("P*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            reels[r["id"]] = r
    return reels


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.replace("|", " ").replace("*", "").lower()).strip("-")[:40]


def main(ids):
    reels = load_all()
    out_root = ROOT / "pilot"
    for n, rid in enumerate(ids, 1):
        r = reels[rid]
        d = out_root / f"{n:02d}-{slug(r['hook'])}"
        d.mkdir(parents=True, exist_ok=True)
        spec = {
            "id": r["id"],
            "hook": r["hook"],
            "speed": 1.05,
            "musicVol": 0.3,
            "outro": r.get("outro", "*The Thread Beneath*"),
            "lines": [{"say": l["say"], "shots": [[s[0], s[1], s[2] if len(s) > 2 else {}] for s in l["shots"]]} for l in r["lines"]],
        }
        (d / "reel.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
        (d / "post.txt").write_text(
            f"{r['id']} · {r['style']} · {r['pillar']} / {r['sub']} · {r['status']}\n\n"
            f"INSTAGRAM\n{r['ig_caption']}\n\nTIKTOK\n{r['tt_caption']}\n\n"
            f"FACT NOTE (internal, do not post)\n{r['fact_note']}\n",
            encoding="utf-8",
        )
        print(d.relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:] or PILOT)
