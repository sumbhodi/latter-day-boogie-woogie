#!/usr/bin/env python3
"""jug.py — Sum, 3 Aug: "how much does a good green data center pay for 1 gallon of denatured water
for a closed loop conservative system? Sure it costs more per gallon, but you need to flush a few
times a DECADE, not a day."

⚠ I HAVE BEEN PRICING WATER AS A FLOW (AF/yr) BECAUSE THAT IS HOW EVERY OTHER USE WORKS.
   A closed loop is not a flow. It is an INVENTORY that gets replaced occasionally.
   Everything changes when you price the inventory instead of the throughput.
"""
IT_MW   = 100
TON_KW  = 3.517
GAL_TON = 6            # loop inventory, gal per ton of cooling (range 3-10)
FLUSH_Y = 3            # "a few times a decade"
MAKEUP  = 0.07         # leaks, drain-downs, maintenance, per year
JUG     = 5.0          # gallons — under the Great Lakes Compact 5.7-gal container exemption
PER_TRK = 300          # "tubes on 300 5-gallon jugs"

tons = IT_MW * 1000 / TON_KW
inv  = tons * GAL_TON
ann  = inv / FLUSH_Y + inv * MAKEUP
evap = IT_MW * 1000 * 1.30 * 8760 * 1.80 / 3.78541      # gal/yr, wet tower

print("=" * 72)
print(f"  A {IT_MW} MW FACILITY — the inventory, not the flow")
print("=" * 72)
print(f"  cooling load                     {tons:>14,.0f} tons")
print(f"  LOOP INVENTORY  (@{GAL_TON} gal/ton)     {inv:>14,.0f} gal   ← filled ONCE")
print(f"  flush every {FLUSH_Y} yr + {MAKEUP:.0%} makeup      {ann:>14,.0f} gal/yr")
print(f"  the same plant on a WET TOWER    {evap:>14,.0f} gal/yr")
print(f"\n  ⭐⭐ RATIO: the closed loop uses 1 / {evap/ann:,.0f} th of the water.")
print(f"     {evap/325851:,.0f} AF/yr  vs  {ann/325851:.2f} AF/yr\n")

print("=" * 72)
print("  WHAT THEY WILL PAY — and why the markup is free money")
print("=" * 72)
print(f"  {'$/gal':>8}{'annual bill':>16}{'% of a $150M/yr facility':>28}")
for p in (0.05, 0.25, 1.00, 2.00, 5.00):
    print(f"  {p:>7,.2f}{ann*p:>15,.0f}{ann*p/150e6*100:>26.3f}%")
print("\n  ⭐ At $2.00/gal — 40x a municipal industrial rate — the bill is a rounding error")
print("     on their P&L. ⚠ AND SO IS OUR REVENUE. Water is NOT the line. Say it plainly.")

print("\n" + "=" * 72)
print("  ⭐⭐⭐ BUT LOOK WHAT FITS THROUGH THE 5.7-GALLON EXEMPTION")
print("=" * 72)
trk = PER_TRK * JUG
print(f"  {PER_TRK} x {JUG:.0f}-gal jugs, automated funnel      {trk:>10,.0f} gal per truck")
print(f"  truckloads to supply one {IT_MW} MW plant   {ann/trk:>10,.0f} per year "
      f"({ann/trk/52:.1f}/week)")
print(f"  truckloads if it ran a WET TOWER        {evap/trk:>10,.0f} per year "
      f"({evap/trk/365:,.0f}/DAY)")
print(f"\n  ⭐⭐ ONE TRUCK, ~{ann/trk/52:.0f} TRIPS A WEEK, SUPPLIES A 100 MW DATA CENTRE —")
print( "     ENTIRELY INSIDE THE CONTAINER EXEMPTION THE BEVERAGE INDUSTRY ALREADY USES.")
print( "  ⚠ The jug was the satire. At closed-loop volumes the satire is simply sufficient.")

print("\n" + "=" * 72)
print("  AND THE TREATMENT RUNS ON CURTAILED POWER")
print("=" * 72)
kwh = ann / 1000 * 10       # ~10 kWh per 1,000 gal, RO + DI polish from a fresh source
print(f"  energy to make a year's supply          {kwh:>10,.0f} kWh = {kwh/1000:.2f} MWh")
print(f"  as a share of the plant's own draw      {kwh/(IT_MW*1000*1.10*8760)*100:>10.5f} %")
print( "  ⭐ RO/DI is a perfectly interruptible load. Make it on negative-price hours.")
print( "     De-natured water is a way to STORE CURTAILED ELECTRICITY AS A PRODUCT.")

print("\n" + "=" * 72)
print("  ⭐⭐⭐ WHERE THE MONEY ACTUALLY IS: THE AVOIDED EVAPORATION")
print("=" * 72)
af = (evap - ann) / 325851
print(f"  water NOT evaporated per converted plant {af:>10,.0f} AF/yr")
for p, tag in ((1303, "WRC @ $4/1,000 gal"), (1171, "our delivered cost"), (2586, "SLC household marginal")):
    print(f"    valued at ${p:,}/AF  ({tag:<22}) ${af*p/1e6:>7,.1f} M/yr")
print(f"\n  ⭐ Every customer we sign is +{af:,.0f} AF/yr to the basin, and the flush goes")
print( "     to the aquifer treated. THE CUSTOMER IS A DEPOSIT, NOT A WITHDRAWAL.")
print(f"  ⚠ That is worth ~{af*1303/(ann*2.0):,.0f}x the water sale. We are not a water")
print( "     company with a data centre. We are a data centre that pays in water.")
