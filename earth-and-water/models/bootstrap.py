#!/usr/bin/env python3
"""bootstrap.py — Sum: "we can truck [denatured water] from Indiana in 5 gallon jugs to make the
data center one happen."

⭐ THE SHORT BILL CREATES THE DEMAND AND THE JUG SERVES IT ON DAY ONE. No pipe, no compact fight,
no $30bn. This checks whether that is actually tractable at Utah's real data-centre load.
"""
TRK, GAL_KW, JUGYR = 1500, 1.706, 0.07 + 1/3   # ⚠ FACILITY inventory (6 gal/ton), not DLC-only     # gal/truck, loop gal per kW, flush+makeup rate
PX, MILES, RATE = 5.00, 1500, 2.50               # $/gal, Indiana->Utah, $/truck-mile

print("=" * 76); print("  THE BOOTSTRAP — serving Utah's data centres by truck"); print("=" * 76)
print(f"  {'Utah DC load':<18}{'initial FILL':>16}{'recurring':>16}{'trucks/day':>13}")
for mw in (100, 500, 1000, 2000):
    fill = mw * 1000 * GAL_KW
    ann  = fill * JUGYR
    print(f"  {mw:>10,} MW   {fill/TRK:>12,.0f} loads{ann/TRK:>12,.0f} /yr"
          f"{ann/TRK/365:>13.2f}")

mw = 1000
fill, ann = mw*1000*GAL_KW, mw*1000*GAL_KW*JUGYR
haul = ann/TRK * MILES * RATE
print(f"\n  ⭐⭐ AT 1 GW OF UTAH DATA-CENTRE LOAD — {ann/TRK/365:.1f} TRUCKS A DAY.")
print(f"     one-time fill  {fill/TRK:,.0f} loads (${fill*PX/1e6:,.1f} M of product)")
print(f"     recurring      ${ann*PX/1e6:,.1f} M/yr revenue  -  ${haul/1e6:,.1f} M/yr haul"
      f"  =  ${(ann*PX-haul)/1e6:,.1f} M/yr")
print(f"  ⚠ haul is {haul/(ann*PX)*100:.0f}% of revenue at {MILES:,} mi. THIN, AND THAT IS THE POINT:")
print( "     trucking works and does not scale. The crossover to a pipe is the story arc.")

print("\n" + "=" * 76); print("  ⚠⚠ THE HOLE, AND WHY IT IS NOT ONE"); print("=" * 76)
print("""  ⚠ Denatured water is MANUFACTURED. RO/DI does not care about the source — you can
     make it from Utah water, in Utah, and skip 1,500 miles of freight.
  ⭐ So the Indiana haul is NOT a water supply. Utah-sourced denatured water is basin
     water; it adds nothing. Indiana-sourced water is NEW TO THE BASIN.
  ⭐⭐⭐ AND THAT IS THE REAL PRODUCT: at 46 truckloads a year you establish the entire
     legal spine — Indiana source, lawful interstate movement under the 5.7-gal container
     exemption, Utah delivery, water credited to the basin — AT A VOLUME NOBODY WILL
     BOTHER TO FIGHT.
  ⭐⭐ Build the precedent at toy scale. Scale the volume later against a settled record.
     ⚠ Which is precisely how the beverage industry established its own position: nobody
        objected while it was small, and by the time it was 120 billion gallons the
        question had been answered for thirty years.""")
