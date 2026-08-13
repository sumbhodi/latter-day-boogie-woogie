# The Veins — free, public-domain sources for the churn

The rule: **canon is copied, never generated.** A bot must never "write a Twain quote" — that's how you get
fake attributions. It scrapes the real text from these, tags it (author · book · theme), and the paper filters it.
Original voice (koans, jokes, wei, the ads/obits/opinion) is the only thing a model *writes*.

## The archives (start here — one place, everything)

| archive | what | how the bot pulls it |
|---|---|---|
| **Gutendex API** — `gutendex.com/books` | 70k+ Project Gutenberg books, JSON metadata, no key | search author → get the plain-text URL → download |
| **Project Gutenberg** — `gutenberg.org/cache/epub/{id}/pg{id}.txt` | the full plain text of any book | one GET per book |
| **Standard Ebooks** — `standardebooks.org` | the same public-domain texts, *clean* (proofed, no PG boilerplate) | best for quotable prose |
| **Sacred-Texts** — `sacred-texts.com` | the canonical PD religion/philosophy/esoterica archive | per-tradition index pages |
| **Sefaria** — `sefaria.org` + `github.com/Sefaria/Sefaria-Export` | Tanakh w/ the **JPS 1917** (public domain) translation, JSON | bulk JSON export |
| **quran-json** — `github.com/risan/quran-json` | full Qur'an + translations (Tanzil), JSON | clone the repo |
| **World English Bible** — `ebible.org` / `bible-api.com` | the Bible, **public domain**, per-verse JSON | bible-api.com/john+3:16 |

## The authors (the quote + shelf lanes)

All on Gutenberg — pull the plain text, split into quotes/passages, tag by author + book:
**Twain · Wilde · Bierce (The Devil's Dictionary) · Dostoevsky · Melville · Whitman · Thoreau · Poe · Emerson ·
Dickinson · Austen · Marcus Aurelius (Meditations) · Emerson · Montaigne.** (Yogi Berra, Vonnegut, Dorothy Parker
are **not** PD — keep those as the small hand-curated set you already have.)

## Spirituality — every tradition represented

- **Zen** — *The Gateless Gate* (Mumon, PD, non-renewed): [sacred-texts.com/bud/glg](https://sacred-texts.com/bud/glg/index.htm) · *101 Zen Stories* (Nyogen Senzaki 1919, PD) on sacred-texts + Internet Archive
- **Taoism** — *Tao Te Ching*, James Legge translation (PD): [Standard Ebooks](https://standardebooks.org/ebooks/laozi/tao-te-ching/james-legge) · also J.H. McDonald's explicitly-PD version
- **Buddhism** — *The Dhammapada* (multiple PD translations, sacred-texts + Gutenberg)
- **Bible** — World English Bible (PD) via ebible.org; Ecclesiastes especially (the great nihilist-adjacent book)
- **Qur'an** — quran-json (Tanzil) + [alquran.cloud API](https://alquran.cloud)
- **Tanakh** — Sefaria, JPS 1917 (PD)
- **Gita** — Edwin Arnold's *The Song Celestial* (PD, Gutenberg) + [vedicscriptures.github.io](https://vedicscriptures.github.io) per-verse
- **Sufism** — Rumi, older PD translations (Whinfield, Nicholson — sacred-texts)
- **Confucianism** — *The Analects*, Legge translation (PD, sacred-texts)
- **Thelema** — Crowley's *Liber AL vel Legis* (public); other Crowley varies — verify each
- **Stoicism** — Marcus Aurelius *Meditations* · Epictetus *Enchiridion* (both PD, Gutenberg)

## Nihilism (you named it)

- **Nietzsche** — *Thus Spake Zarathustra* ([Gutenberg #1998](https://www.gutenberg.org/ebooks/1998)), *Beyond Good and Evil*, *The Gay Science*, *Twilight of the Idols* — all PD
- **Schopenhauer** — *Studies in Pessimism*, *The Wisdom of Life* (PD, Gutenberg)
- **Ecclesiastes** — "vanity of vanities" (the WEB Bible, PD)

## The theme-rotation feature (Sum's idea — the harmony machine)

Tag every canon piece with a **theme** (impermanence · patience · the self · death · joy · letting go …). Then the
paper can rotate ONE theme/day and show the **Bible verse + the Crowley line + the Gita śloka + the Zen koan that all
say the same thing** — cross-tradition harmony. "Easier than finding disagreements, and truer." Needs: a theme tag on
each piece (the flagship bot does this well while it scrapes) + a "today's theme" picker in the paper.

*Sources this session: [Gutendex](https://gutendex.com/) · [Gateless Gate (sacred-texts)](https://sacred-texts.com/bud/glg/index.htm) · [Nietzsche, Gutenberg #1998](https://www.gutenberg.org/ebooks/1998) · [Tao Te Ching, Standard Ebooks](https://standardebooks.org/ebooks/laozi/tao-te-ching/james-legge)*

## Water price — the reference numbers (verified 12 Aug 2026)

Salt Lake City Public Utilities, FY27 schedule, effective 1 July 2026 —
<https://www.slc.gov/utilities/fy27rates/>. One acre-foot = 435.6 CCF.

| rate class | per CCF | per acre-foot |
|---|---|---|
| commercial / industrial · summer (Apr–Oct) | $4.18 | **$1,821** |
| commercial / industrial · winter | $2.58 | $1,124 |
| household top tier | $5.94 | $2,586 |

$1,821/AF is the reference rate DUST uses. These figures match the ones already carried in
plan.html, so the whole site quotes one set.

**Still to source — the rights-holder side.** What an acre-foot actually costs a rights
holder per year (irrigation company assessments, conservancy district rates, delivery
charges). The spread between that and $1,821 is the load-bearing figure of the DUST
argument, so it gets a URL and a date before it gets printed.

## Elevations — the bench corridor (verified 13 Aug 2026)

USGS Elevation Point Query Service, <https://epqs.nationalmap.gov/v1/json>, feet, WGS84.

| point | ft | | point | ft |
|---|---|---|---|---|
| Great Salt Lake | 4,195 | | State Capitol | 4,533 |
| Rose Park | 4,216 | | Univ. of Utah | 4,781 |
| SLC Airport | 4,220 | | Foothill bench | 4,825 |
| Bountiful flats | 4,232 | | Olympus Cove | 4,933 |
| Farmington Bay | 4,203 | | Ensign Peak | 5,059 |
| Ogden flats | 4,298 | | Bountiful bench | 5,194 |
| Layton flats | 4,353 | | **Farmington bench** | **5,951** |
| Emigration mouth | 5,168 | | Emigration upper | 5,960 |
| Millcreek mouth | 5,083 | | Millcreek upper | 6,840 |
| | | | Jordanelle | 6,145 |

Working head: Farmington **1,748 ft** · Bountiful 962 · Avenues→Rose Park 843 ·
Kaysville 658 · Ogden 446 · Layton 280 · Capitol→Airport only **313** (too little).
Jordanelle→valley 1,925 ft, but 25 miles away over existing conveyance.

⚠ Millcreek (1,757 ft) and the Cottonwoods are protected drinking-water watershed —
head that exists and is not available. Kept out of the corridor table on purpose.
