#!/usr/bin/env python3
"""mangrove.py — Sum: "under mangrove greenhouse, or anything tropical: salt water floor,
walkways and beds above. Heat, evap, humidity, water at bottom gets saltier. Slant the roof
and collect?"

He has described a SOLAR STILL with a mangrove swamp in it, fed on Great Salt Lake brine and
heated by servers. It works. Two things bite, and both are fixable in the section.
"""
MI, AC = 25, 2.0                 # segment miles, acres of salt floor per mile
EVAP_MM = 10.0                   # mm/day from a 35 C brine surface into moving 20 C air
BRINE_GL = 140.0                 # g/L, Great Salt Lake south arm (north arm runs near 270)
M2 = AC * 4046.86 * MI
L_day = M2 * EVAP_MM
print("=" * 78); print("  THE STILL — one 25-mile segment"); print("=" * 78)
print(f"  salt-water floor                     {AC*MI:>12,.0f} acres  ({M2:,.0f} m2)")
print(f"  evaporation @ {EVAP_MM:.0f} mm/day            {L_day:>12,.0f} L/day"
      f"  ({L_day/3.78541:,.0f} gal/day)")
print(f"  FRESH WATER CONDENSED                {L_day*365/1_233_482:>12,.0f} AF/yr")
feed = L_day / (1 - BRINE_GL/1000)
salt = feed * BRINE_GL / 1000
print(f"  brine fed to supply it               {feed:>12,.0f} L/day")
print(f"  SALT LEFT BEHIND                     {salt/1000:>12,.0f} tonnes/day"
      f"  ({salt*365/1e6:,.0f} kt/yr)")

print("\n" + "=" * 78); print("  ⭐⭐⭐ WHAT THAT ACTUALLY IS, IN THE LAKE'S ACCOUNTING")
print("=" * 78)
print("  Mineral extraction today: take lake water -> evaporate to sky -> keep salt.")
print("  This machine:             take lake water -> CONDENSE AND RETURN -> keep salt.")
print("  ⭐ Same product. Same salt. The water comes back instead of going up.")
print("  ⭐⭐ And it removes SALT from a lake that is currently too saline for brine shrimp —")
print("     so it is also a salinity lever, which 73-32-408(7) already zones for.")
print("  ⚠ A LEVER, NOT A FREE GOOD. The lake must stay saline. Over-desalting is its own")
print("     failure mode and the bill's measurement loop is what should set the rate.")

print("\n" + "=" * 78); print("  ⚠⚠ THE TWO THINGS THAT BITE"); print("=" * 78)
print("""  1. DO NOT CONDENSE OVER THE CROP.
     A solar still works because nothing grows under it. Condensate dripping on leaves
     spreads Botrytis and mildew, and film on the glazing steals light.
     ⭐ Seawater Greenhouse — running this in deserts for 20 yr — does NOT condense on the
        roof. It evaporates at ONE END and condenses at the OTHER, crop in the middle in
        cooled, part-dried air. THE-ENVELOPE already put the condenser on the cold OUTER
        skin. Keep it there. The slant is right; slant it TOWARD that wall.
     ⚠ If you do want a cold roof, it needs anti-drip (hydrophilic) glazing so condensate
        SHEETS to the gutter instead of beading and dropping. Standard commercial film.

  2. SALT AEROSOL.
     Evaporating brine indoors puts chloride in the air: corrodes structure and fixings,
     burns leaves, films the glass. Mangroves do not care — they excrete salt already.
     ⚠ Everything else does. Stainless/FRP in the evaporator zone, and a physical
        separation between the brine bay and the beds.""")

print("\n" + "=" * 78); print("  ⭐ AND WHY MANGROVE IS THE RIGHT PLANT AND NOT A JOKE")
print("=" * 78)
print("""  Red mangrove is a true halophyte — it grows in full-strength seawater, which nothing
  else you would want to look at will do. It is the only canopy that can stand IN the
  evaporator instead of beside it.
  ⚠ It is also strictly tropical: no frost, >20 C year round. In Utah that is a winter
     heat load forever — ⭐ which is exactly the load we have been trying to find a customer
     for since THE-GRADIENT. The hardest plant to keep alive here is the one that wants
     precisely what we cannot sell.
  ⚠ HONEST: this is habitat-shaped, but it is NOT Great Salt Lake habitat. GSL birds eat
     brine shrimp and brine flies. Do not let a rendering imply we are building bird
     habitat — 408(7) does that with open water, not under glass.""")
