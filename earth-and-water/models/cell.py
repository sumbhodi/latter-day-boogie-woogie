#!/usr/bin/env python3
"""cell.py — Sum: "spec out a 5 gallon closed loop system, how big it is, like how much ram
and flops."

⚠ THE ANSWER DEPENDS ENTIRELY ON WHICH LOOP YOU MEAN, and the gap is 11x. Both are stated.
   A facility chilled-water plant carries a huge thermal inventory (buffer tanks, long mains).
   A direct-to-chip loop carries almost none — which is the whole point of DLC, and it is the
   architecture a jug-fed system would actually be.
"""
JUG = 5.0
ANCHOR = dict(name="NVIDIA GB200 NVL72", kw=120, gpus=72, hbm_tb=13.5, pflops_fp4=1440)

print("=" * 74); print("  WHAT DOES 5 GALLONS COOL?"); print("=" * 74)
for tag, gal_per_kw, note in [
        ("facility chilled-water loop", 6/3.517, "6 gal/ton, incl. buffer + mains"),
        ("DIRECT-TO-CHIP loop",         0.15,    "CDU + cold plates, no buffer")]:
    kw = JUG / gal_per_kw
    print(f"  {tag:<30}{gal_per_kw:>7.3f} gal/kW  ->  {kw:>7.1f} kW per jug   ({note})")

kw = JUG / 0.15
A = ANCHOR
print(f"\n  taking the DLC case — {kw:.1f} kW per five-gallon jug")
print(f"  anchored on {A['name']}: {A['kw']} kW, {A['gpus']} GPUs, "
      f"{A['hbm_tb']} TB HBM, {A['pflops_fp4']:,} PFLOPS FP4\n")
r = kw / A['kw']
print(f"  ⭐ ONE FIVE-GALLON JUG COOLS:")
print(f"       GPUs                     {A['gpus']*r:>10.1f}")
print(f"       HBM memory               {A['hbm_tb']*r*1000:>10,.0f} GB  ({A['hbm_tb']*r:.2f} TB)")
print(f"       compute, FP4             {A['pflops_fp4']*r:>10,.0f} PFLOPS")
print(f"       compute, FP8 (~half)     {A['pflops_fp4']*r/2:>10,.0f} PFLOPS")

print("\n" + "=" * 74); print("  ⚠ SANITY CHECK — inventory is not what carries the heat, FLOW is")
print("=" * 74)
CP, DT = 4.18, 10.0
mdot = kw / (CP * DT)
gpm = mdot * 60 / 3.78541
print(f"  {kw:.1f} kW at a {DT:.0f} C rise needs {mdot:.2f} kg/s = {gpm:.1f} gal/min")
print(f"  a {JUG:.0f}-gal inventory at {gpm:.1f} gpm turns over every {JUG/gpm*60:.0f} seconds.")
print("  ⭐ That is an ordinary loop turnover. The spec is coherent — the jug is the CHARGE,")
print("     the pump is the capacity. Five gallons is not a small tank, it is a whole loop.")

print("\n" + "=" * 74); print("  THE STACK — how many jugs is a real deployment"); print("=" * 74)
for tag, kwt in [("one GB200 NVL72 rack", A['kw']), ("a 12-rack row", A['kw']*12),
                 ("1 MW hall", 1000), ("a 100 MW campus", 100_000)]:
    jugs = kwt * 0.15 / JUG
    print(f"  {tag:<24}{kwt:>9,.0f} kW ->{jugs:>10,.0f} jugs   ({jugs/300:>7.1f} truckloads)")
print("\n  ⭐ ONE RACK = ~4 JUGS. That is the unit. It stacks and rows because the RACK does.")
print("  ⚠ and those are FILL numbers, paid once. The recurring need is the flush:")
print(f"     a 100 MW campus re-charges every 3 yr + 7%/yr makeup = ~46 truckloads A YEAR.")
