#!/usr/bin/env python3
"""brine.py — Sum: "can we use this waste heat to de-sal and HARVEST not dump the brine too?"

Yes — and the answer is far more load-bearing than the question, because the Great Salt Lake's
mineral industry does not have a brine DISPOSAL problem. It has a brine CONCENTRATION method,
and the method is SOLAR EVAPORATION PONDS. Their entire process is deliberately boiling the lake.
"""
print("=" * 78); print("  WHAT THE MINERAL INDUSTRY ACTUALLY DOES TO THE LAKE"); print("=" * 78)
F = [("solar evaporation ponds, Compass + US Magnesium", "110,000+ acres"),
     ("once evaporated annually",                        "270,000 AF/yr"),
     ("Compass Minerals, avg depletion 2017-2021",       "111,700 AF/yr"),
     ("one company, 2024 alone",                         "52,455 AF  (>100,000 households)"),
     ("share of depletion that would otherwise reach lake","7-13%  ⚠ baseline-dependent"),
     ("Lilac Solutions filing, claims full return",       "225,000 AF")]
for a, b in F: print(f"  {a:<50}{b}")
print("\n  ⭐⭐⭐ THE POINT: a solar evaporation pond is not a byproduct. It IS the process.")
print("     They are paying the lake, in water, to concentrate brine that waste heat could")
print("     concentrate for free. It is the single most substitutable use on the whole ledger.")

print("\n" + "=" * 78); print("  DOES OUR GRADE OF HEAT ACTUALLY RUN A CRYSTALLISER?"); print("=" * 78)
print(f"  {'process':<34}{'works at':>14}{'notes':>28}")
for n, t, note in [("HDH (humid-dehumidification)", "40-90 C", "sub-boiling, waste heat"),
                   ("membrane distillation (MD)",   "40-80 C", "handles HIGH salinity"),
                   ("MD + crystalliser (MDC)",      "~65 C",   ">95% recovery, salt slurry"),
                   ("low-temp MED",                 "55-70 C", "above our raw grade"),
                   ("conventional MSF",             "90-120 C","⚠ out of reach")]:
    print(f"  {n:<34}{t:>14}{note:>28}")
print("\n  our raw data-centre return              30-45 C   ⚠ low end of the window")
print("  salt crystallisation rate, 40 C ->  7.5 kg per m3 of feed")
print("                             70 C -> 34.0 kg per m3   ⭐ 4.5x for 30 C of lift")
COP, LIFT = 4.5, 30
print(f"\n  ⭐ a heat pump lifting 40 C -> 70 C runs at COP ~{COP}: {1/COP:.2f} kWh in per kWh")
print(f"     of heat delivered. On our own curtailed power that lift is nearly free, and it")
print(f"     buys {34/7.5:.1f}x the crystallisation. ⭐⭐ LIFT THE HEAT, DO NOT USE IT RAW.")

print("\n" + "=" * 78); print("  ⭐⭐⭐ AND THE ENVELOPE IS ALREADY AN HDH MACHINE"); print("=" * 78)
print("  HDH desalination = humidify warm air over brine, condense on a cold surface.")
print("  THE-ENVELOPE just built exactly that and called it a jungle house:")
print("     warm humid core (data-centre heat)  ->  cold outer glazing (the cold pipe)")
print("  ⭐ We did not design a desalination plant. We designed a greenhouse and it turned")
print("     out to be one. Seawater Greenhouse has run this in deserts for twenty years.")

print("\n" + "=" * 78); print("  ⚠⚠ AND IT IS ALREADY IN THE BILL, BY ACCIDENT"); print("=" * 78)
print("  73-32-410(2)(d), drafted this morning to be about cooling towers, says:")
print('     "a use that returns no portion of the water applied to the waters of the basin')
print('      is a greater consumptive use than a use that returns a portion, WITHOUT REGARD')
print('      to the purpose of either use or to the classification of the user."')
print("\n  ⚠ A solar evaporation pond is the purest zero-return use on the lake, and that")
print("     sentence is written generally enough to name it without naming it.")
print("  ⚠⚠ DECIDE THIS ON PURPOSE. Either it is aimed at the ponds — and the bill takes on")
print("     the mineral lobby — or it needs a carve. It must not be an accident nobody chose.")
