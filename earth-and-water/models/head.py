#!/usr/bin/env python3
"""head.py — MADE head vs FOUND head. Sum, 3 Aug: "I went to school in indiana, there are many
water towers and hills. dig and berm add tower for storage on chicago loop."

He is correcting an error I made: I priced the Chicago spur on ENDPOINT ELEVATION (Indiana ~700 ft,
Chicago ~580) and called it 120 ft. Pumped storage does not care about endpoints. It cares about
LOCAL RELIEF — two reservoirs near each other with vertical separation. Completely different number.
"""
KWH = 1.025          # kWh per acre-foot per foot of head
RHO_G = 1000 * 9.81

def energy(acres, swing_ft, head_ft):
    af = acres * swing_ft
    return af, af * head_ft * KWH / 1000          # MWh

def flow_for(mw, head_ft, eff=0.90):
    return mw * 1e6 / (RHO_G * head_ft * 0.3048 * eff)   # m3/s

print("=" * 74)
print("  FOUND HEAD — southern Indiana, unglaciated, the half we can legally use")
print("=" * 74)
# Weed Patch Hill, Brown County: 322 m elevation, 83 m PROMINENCE = 272 ft of local relief
# Salem Limestone quarries, Bedford-Bloomington belt: 90 ft deep, vertical walls, already flooded
for name, acres, swing, head in [
        ("quarry pair, Salem Limestone",  27.5,  60, 300),
        ("quarry + ridge pond, Brown Co", 27.5,  60, 272),
        ("big quarry pair",              120.0,  70, 300)]:
    af, mwh = energy(acres, swing, head)
    print(f"  {name:<32} {af:>7,.0f} AF  {head:>4.0f} ft ->{mwh:>7,.0f} MWh"
          f"  ({mwh/100:>4.1f} h @ 100 MW)")

print()
print("=" * 74)
print("  MADE HEAD — dig and berm, flat ground, balanced cut and fill")
print("=" * 74)
# 1 km x 1 km pond. dig 10 m -> 10.0M m3 of spoil.
# ring berm 15 m high, 8 m crest, 3:1 slopes: 15*(8+45)=795 m2 x 4,000 m perimeter = 3.18M m3
dig_m3 = 1_000_000 * 10
berm_m3 = 4_000 * (15 * (8 + 3*15))
print(f"  spoil from digging 10 m over 1 km^2   {dig_m3/1e6:>6.2f} M m3")
print(f"  fill needed for a 15 m ring berm      {berm_m3/1e6:>6.2f} M m3")
print(f"  -> balances {dig_m3/berm_m3:.1f}x over. ⭐ DIG-AND-BERM IS SELF-SUPPLYING.")
af, mwh = energy(247, 60, 82)
print(f"  247-acre pair, 82 ft made head        {af:>7,.0f} AF ->{mwh:>7,.0f} MWh"
      f"  ({mwh/100:>4.1f} h @ 100 MW)")

print()
print("=" * 74)
print("  ⚠ THE LOW-HEAD PENALTY — cheap MWh, expensive MW")
print("=" * 74)
print(f"  {'head':>10}{'flow for 100 MW':>20}{'machine size vs 700 ft':>26}")
base = flow_for(100, 700)
for h in (82, 175, 272, 300, 700):
    q = flow_for(100, h)
    print(f"  {h:>8} ft{q:>17,.0f} m3/s{q/base:>22.1f}x")
print("  ⭐ but a data centre buys HOURS, not megawatts. The penalty lands on the axis")
print("     that matters least. 4-8 h of ride-through and arbitrage, not frequency response.")

print()
print("=" * 74)
print("  ⚠ AND THE ONE THAT DOES NOT SURVIVE: the water tower as a battery")
print("=" * 74)
af = 2_000_000 / 325_851
mwh = af * 175 * KWH / 1000
print(f"  2 M gal tower at 175 ft = {af:.2f} AF = {mwh*1000:,.0f} kWh = {mwh:.2f} MWh")
print(f"  a 100 MW load eats that in {mwh/100*3600:.0f} SECONDS.")
print(f"  towers needed for one 8-hour node: {100*8/mwh:,.0f}")
print("  ⭐ so a tower is not storage. It is 40 s of GRAVITY-FED COOLING that survives a")
print("     total power loss — which is the exact window a UPS bridges. Sell it as that.")

print()
print("=" * 74)
print("  ⭐⭐ THE COOLING STACK — and I had it upside down")
print("=" * 74)
print("  Sum: 'you are underselling the green powered denatured water for closed loop.")
print("        cooling tower is a 4 letter word. we do not sell potable water to data")
print("        centers, that should be illegal.'")
print()
IT = 100                       # MW of IT load
HRS = 8760
for name, pue, l_per_kwh in [
        ("evaporative tower  (the norm)", 1.30, 1.80),
        ("dry / air cooled   (the fix)",  1.40, 0.05),
        ("once-through COLD PIPE (ours)", 1.10, 0.00)]:
    over = IT * (pue - 1)
    twh = IT * pue * HRS / 1000
    litres = IT * 1000 * pue * HRS * l_per_kwh
    af = litres / 1_233_482
    print(f"  {name:<32} PUE {pue:.2f}  overhead {over:>5.1f} MW"
          f"  water {af:>7,.0f} AF/yr")
print()
ev = IT * 0.30; ot = IT * 0.10
saved = (ev - ot) * HRS
print(f"  ⭐ once-through vs the tower: {ev-ot:.0f} MW less overhead = {saved/1000:,.0f} GWh/yr")
for p in (45, 60, 90):
    print(f"     worth to the tenant @ ${p}/MWh:  ${saved*p/1e6:>6,.1f} M/yr")
evap_af = IT*1000*1.30*HRS*1.80/1_233_482
print(f"  ⭐ and it stops consuming {evap_af:,.0f} AF/yr — a town of "
      f"{evap_af*325851/365/100:,.0f} people at 100 gal/day.")
print()
print("  ⚠ THE POINT I MISSED: closed-loop is normally a SACRIFICE — you give up the")
print("     latent heat of vaporisation and your PUE gets worse. That is why the industry")
print("     uses towers. But we are not dry cooling. We have a COLD PIPE, so we beat the")
print("     tower on BOTH axes at once. It is not abstinence. It is a better machine.")
