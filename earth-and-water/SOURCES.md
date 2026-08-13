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

## ⚠ NUMBERS THAT ARE NOT YET SOURCED (flagged 12 Aug 2026)

**~$2,851/AF peak commercial municipal rate** — SUM'S ESTIMATE, recalled once from a single
reading days ago, mid-session, across a very long conversation. It is a memory of a number,
not a citation. **It is also the load-bearing figure of the entire DUST bill** — the spread
between it and the rights-holder price IS the argument. Do not print it, quote it to a
reporter, or hand it to a clinic until it is replaced by a rate schedule with a URL and a
date. Same standard for the ~$300/AF rights-price side of the spread.
