# The Thread Beneath: 100 Reels / TikToks

Scris pe 14 oct 2026, în colaborare cu sesiunea „The Thread Beneath” (care are planul, uneltele și fișierele de pe laptop). Textul reel-urilor e în engleză, pentru publicul din SUA.

## 1. Ce am aflat din research

Am folosit vidIQ: reel-uri și TikTok-uri din iul–oct 2026 care au făcut de 5–800× mai multe vizualizări decât media creatorului. Nișele căutate: mistere istorice, viața de după moarte, Tesla și geometrie sacră, hook-uri.

| Ce merge | Exemplu (vizualizări, × față de media creatorului) | Ce luăm de aici |
|---|---|---|
| Narațiune documentar + dovezi pe ecran | Göbekli Tepe, 70K (29×) · Antikythera, 128K (30×) · mica de la Teotihuacan (12×) | Stilul S1 „Cold Case” |
| O singură imagine istorică, povestită | Nuremberg 1561, 3,3M (117×) · fotografia din 1901 (175×) | Stilul S2 „One Image” |
| Listă scurtă | „3 obiecte găsite în rocă”, 116K (41×) | Stilul S3 „Countdown” |
| Mit corectat cu dovezi | „Golden ratio nu era «divin» la început”, 193K (110×) | Stilul S4 „Myth vs Record” |
| Citat sau text vechi, citit cu voce | Tesla 3‑6‑9, 1,1M · Ea‑nasir (meme clasic) | Stilul S5 „Voice from the Past” |
| „What if” filozofic cu artă AI | „What if dying is waking up…”, 1,1M (161×) | Stilul S6 „What If” (artă AI declarată) |
| Caz concret: om, dată, ce s-a întâmplat | NDE-ul profesorului (92×) · apelurile din 1994 (187×) | Stilul S7 „Case File” |
| Explicat simplu, cu diagramă | cimatica, 942K · „toate trenele de val au 39°”, 3,7M | Stilul S8 „Made Simple” |
| Scară, timp, comparații | (format clasic Kurzgesagt / Sagan) | Stilul S9 „Scale” |
| Două subiecte legate (semnătura TTB) | — | Stilul S10 „The Thread” |

**Ce contează pentru algoritm:** pe Instagram, Mosseri a confirmat trei semnale de top: timpul de vizionare, like-urile raportate la reach și trimiterile prin DM raportate la reach. Primele 3 secunde decid dacă omul rămâne. Reel-ul trebuie să dea răspunsul complet; asta crește și vizionările repetate și trimiterile. Cuvintele-cheie din descriere ajută la căutare mai mult decât hashtag-urile.

**Hook-urile care merg** (din outlieri):
- **cifră + timp + o afirmație concretă:** „12,000 years ago someone carved…”;
- **„For a century, no one knew what was hidden inside it.”;**
- **o întrebare la persoana I:** „My biggest question will always be…”.

## 2. Regulile (din planul TTB, actualizarea din 14 oct)

- **35–60 s**, narat de Brian v4, cu titlul-hook simplu din primul cadru și subtitrări mari.
- **Răspunsul complet e în reel.** Niciodată „watch the full video on YouTube”.
- **Cadrele ilustrează exact fraza spusă;** niciun montaj la întâmplare.
- **Descrierile sună uman,** scrise de tine pe loc: fără „Source:”, fără întrebări-momeală, 0–3 hashtag-uri, structura variază.
- **Onestitate:** fiecare afirmație are eticheta KNOWN, DEBATED sau SPECULATION. Arta AI e doar ilustrativă și declarată.
- **Imaginile CC BY se creditează pe imagine**, nu în descriere. Fără imagini de la British Museum sau Gallica în conținut monetizat.

## 3. Pilonii și subcategoriile (10 × 10 = 100)

| # | Pilon | Subcategorii |
|---|---|---|
| P01 | Ancient history & lost civilizations | Sumer, megaliți, tehnologie antică, Egipt, mituri istorice |
| P02 | Afterlife & near-death experiences | studii clinice NDE, texte antice despre moarte, creierul care moare |
| P03 | Reincarnation & past lives | cazuri de copii, cercetarea UVA, tradiții religioase, sceptici |
| P04 | Spirits, ghosts & apparitions | știința „bântuirilor”, istoria spiritismului, fotografii celebre, povești antice |
| P05 | God, myths & sacred texts | texte pierdute și regăsite, primii autori, mituri și originile lor |
| P06 | Universe & cosmos | originea elementelor, semnale, scară, misterele cosmologiei |
| P07 | Other dimensions & the physics of reality | cuantic, relativitate, dimensiuni, simulare |
| P08 | Vibration, sound & Tesla | Tesla (mit vs realitate), cimatică, rezonanță, frecvențe „sacre” |
| P09 | Numbers, numerology & sacred geometry | φ, Fibonacci, Pitagora, gematria, numere sacre |
| P10 | Mind, meditation, consciousness & biology | meditația, conștiința, creierul, corpul, mintea animalelor |

Fiecare pilon amestecă 5–8 stiluri, ca să vedem din analytics ce merge. **Fiecare stil apare exact de 10 ori.**

**Ce am schimbat după răspunsul sesiunii TTB:**
- Nu repetăm ce e deja făcut ca short-form: Ea‑nasir, Kushim, stardust, Inanna, medicina babiloniană a fantomelor, cele „5 afterlives”.
- Reel-urile legate de episoadele lungi (Leininger, AWARE, Pam Reynolds, van Lommel, gamma surge) rămân, fiecare cu răspunsul complet.
- „Psychology of deception” a devenit „Mind, meditation, consciousness & biology”.
- Fără actori din stock: cadrele arată locuri, obiecte, arhive, line art.
- 2–3 cadre pe frază, cu gradele TTB: warm, orange, red, magenta, teal, mono, cool.
- Fără artă AI plătită în pilot.

## 4. Fișierele

- `reels/P01…P10.json`: reel-urile, compatibile cu `make-reel.mjs`.
  - Câmpurile scriptului: `hook`, `lines[].say`, `lines[].shots`, `outro`.
  - Câmpurile în plus: `id`, `pillar`, `sub`, `style`, `status`, `fact_note`, `ig_caption`, `tt_caption`.
  - Cadrele sunt **descrieri + termeni de căutare** (`q: …`). Sesiunea TTB le înlocuiește cu fișiere reale (Envato, arhive) înainte de randare.
- `CATALOG.md`: toate cele 100, ușor de citit pe telefon (se generează cu `python3 tools/build_catalog.py`).
- `pilot/NN-slug/`: `reel.json` (pentru `make-reel.mjs`) + `post.txt` (descrierile IG și TikTok + nota internă), generate cu `python3 tools/export_pilot.py [ID…]`.
- `tools/check_reels.py`: verifică lungimea (cuvinte → secunde), câmpurile și regulile de copy (de exemplu, fără „Source:” sau „watch on YouTube”).

## 5. Ce urmează

1. **Pilot (`pilot/`):** 10 reel-uri, câte unul din fiecare stil, deja exportate în formatul `make-reel.mjs`.
   - Sunt: Göbekli Tepe, The Nightmare (Fuseli), van Lommel, Einstein & God, fantoma lui Pliniu, Zhuangzi, Leininger, infrasunetul, „your heart stops”, „why 60 minutes”.
   - Necesită ~7k caractere ElevenLabs. Sesiunea TTB mai are ~64k până pe 9 nov.
2. **După 7–10 zile:** comparăm, în vidIQ și Instagram Insights, timpul de vizionare, trimiterile și salvările pe stil.
3. **Restul:** ritmul de 2–4 pe zi, cu mai multe din stilurile câștigătoare.
4. **Atenție la ElevenLabs:** toate cele 100 înseamnă **73.7k caractere**, adică ~56% din cota lunară Creator (131k), pe care o folosesc și episoadele. Sesiunea TTB propune: pilotul acum, restul după resetarea din 9 nov. Tu decizi ritmul.
5. **Licențe semnalate în `fact_note`:**
   - Brown Lady (1936): poate fi încă sub copyright, deci o redesenăm.
   - Obiectele de la British Museum (Lycurgus Cup, Cyrus Cylinder, tăblițe): imagini non-BM sau redesenare.
   - Filmul Tacoma și interiorul Hypogeum: licența trebuie verificată.
