#!/usr/bin/env python3
"""node.py — the STANDALONE node. Sum, 3 Aug: "we can start with $1b projects in a lot of little
places... data centers that add power to grid and replenish not extract."

model.py assumed 32 segments in ONE line to ONE lake. This asks a different question: does a SINGLE
segment stand up on its own, in Oklahoma, with no lake at the end and no corridor behind it?

⚠ THE CHANGE THAT MATTERS: with no Salt Lake City at the end there is no $1,639/AF municipal buyer.
   The water is recharged, not sold. So this model deletes the water margin entirely and asks
   whether POWER + COOLING + HEAT carries a $1bn asset by themselves.
"""
N = dict(
    capex=1_000_000_000,
    miles=25,
    af_yr=31_250,          # 1M AF / 32, same unit as the corridor segment
    mw=72.7,               # 2,326 MW / 32 sellable average
    heat_twh=0.64,
    heat_mwh=25.0,
    dc_mw=100,             # tenant load on the pump station
)

def line(label, v, note=""):
    print(f"  {label:<34}${v/1e6:>8,.1f} M/yr   {note}")

print("THE STANDALONE NODE — one segment, Oklahoma, no lake at the end\n")
print(f"  capital ${N['capex']/1e9:.2f} bn · {N['miles']} mi · {N['af_yr']:,} AF/yr · "
      f"{N['mw']:.1f} MW sellable · {N['dc_mw']} MW tenant\n")

for tag, pmwh in (("A. merchant power  $45/MWh", 45.0),
                  ("B. time-to-power   $75/MWh", 75.0)):
    print(f"{tag}")
    p = N['mw'] * 8760 * pmwh
    h = N['heat_twh'] * 1e6 * N['heat_mwh']
    # replenishment credit: WRC market clears ~$4 / 1,000 gal = $1,303/AF.
    # ⚠ only the fraction NOT recovered and NOT legally required can be certified.
    cred = N['af_yr'] * 0.5 * 1303
    line("power", p)
    line("waste heat down the ladder", h)
    line("replenishment credit (50% eligible)", cred, "⚠ thin market, see note")
    tot = p + h + cred
    line("TOTAL", tot)
    print(f"  {'cash yield on capital':<34}{tot/N['capex']*100:>9.2f} %"
          f"        payback {N['capex']/tot:>4.1f} yr\n")

# what the corridor's water margin was actually worth, for contrast
marg = N['af_yr'] * (1639 - 1171)
print(f"  for contrast — the corridor's WATER margin on the same segment: ${marg/1e6:,.1f} M/yr")
print(f"  which is {marg/(N['mw']*8760*45)*100:.0f}% of the power line at $45/MWh.")


# ── THE OVERBUILD ─────────────────────────────────────────────────────────────────────────────
# Sum, 3 Aug: "closed loop ethically harvested water and green power and storage at 1.5x your
# estimated peak need. In year one that is like 150% of cost, in 5 years it's a cash flow blip,
# in 10 the investors are thanking you."
#
# ⚠ HIS PREMISE IS WRONG IN OUR FAVOUR. 1.5x capacity does NOT cost 1.5x, because the expensive
#    half of a node does not scale with capacity at all.
print("\n" + "=" * 74)
print("  THE OVERBUILD — 1.5x peak need, and what it actually costs")
print("=" * 74)
FIXED = 0.45   # right-of-way, permitting, interconnect, mobilisation, intake works, the trench
SCALE = 0.55   # solar, pump-turbines, pond, transformers, conductor
BASE_CAP, BASE_REV, BASE_MW = 1_000_000_000, 84_100_000, 72.7

print(f"  fixed capital (ROW, permits, interconnect, trench, intake)  {FIXED*100:.0f}%")
print(f"  capacity-scaling capital (solar, turbines, pond, wire)      {SCALE*100:.0f}%\n")
print(f"  {'build':>8}{'capital':>12}{'MW':>8}{'$/MW':>11}{'revenue':>12}{'yield':>9}")
for x in (1.0, 1.25, 1.5, 2.0):
    cap = BASE_CAP * (FIXED + SCALE * x)
    rev = BASE_REV * x
    print(f"  {x:>6.2f}x{cap/1e9:>11,.3f}B{BASE_MW*x:>8.1f}"
          f"{cap/(BASE_MW*x)/1e6:>10,.2f}M{rev/1e6:>11,.1f}M{rev/cap*100:>8.2f}%")

x = 1.5
extra_cap = BASE_CAP * SCALE * (x - 1)
extra_rev = BASE_REV * (x - 1)
base_yield = BASE_REV / BASE_CAP
print(f"\n  ⭐ 1.5x CAPACITY COSTS {(FIXED+SCALE*x):.3f}x MONEY — 50% more asset for "
      f"{(FIXED+SCALE*x-1)*100:.1f}% more capital.")
print(f"  ⭐ unit cost falls from ${BASE_CAP/BASE_MW/1e6:.2f}M/MW to "
      f"${BASE_CAP*(FIXED+SCALE*x)/(BASE_MW*x)/1e6:.2f}M/MW — {(1-(FIXED+SCALE*x)/x)*100:.0f}% cheaper per MW.")
print(f"\n  the increment:  ${extra_cap/1e6:,.0f} M of capital buying ${extra_rev/1e6:,.1f} M/yr at full use")
print(f"  to clear the base {base_yield*100:.2f}% yield it must earn ${extra_cap*base_yield/1e6:,.1f} M/yr")
print(f"  ⭐⭐ BREAK-EVEN UTILISATION ON THE OVERBUILD: "
      f"{extra_cap*base_yield/extra_rev*100:.0f}%")
print("\n  ⚠ So the question is not 'will the extra sell'. It is 'will MORE THAN HALF of it")
print("     ever sell' — against a 2,600 GW queue and demand forecasts that have been wrong")
print("     LOW every single year. ⭐ That is a cheap option, and year 1 is when it is cheapest.")
print("  ⚠ THE DOWNSIDE, NAMED: if it never sells it is a stranded asset, which is the one")
print("     real risk Sum identified himself. The 55% is what makes it a bet and not a hope.")
