#!/usr/bin/env python3
"""envelope.py — Sum: "start building our own envelopes in waves of thickness around the easement,
all share and move heat air water etc — outer greenhouse, inner greenhouse, jungle greenhouse by
sauna and steam room."

He has turned THE-GRADIENT's heat ladder from a LIST OF CUSTOMERS into a FLOOR PLAN. Nested
thermal zones, hottest at the core. This checks whether nesting actually pays, two ways:
envelope area, and driving temperature difference.
"""
H, AMB = 40.0, 5.0                     # storey height ft, winter ambient C
Z = [("outer greenhouse",  150, 12),   # width ft, setpoint C — coolest, buffers everything
     ("inner greenhouse",  100, 20),
     ("jungle house",       60, 28),
     ("sauna / steam",      20, 80)]   # smallest volume, highest grade, most buffered

print("=" * 76); print("  THE NESTED SECTION — per linear foot of corridor"); print("=" * 76)
print(f"  {'zone':<20}{'width':>8}{'setpoint':>10}{'ΔT if DETACHED':>17}{'ΔT when NESTED':>17}")
for i, (n, w, t) in enumerate(Z):
    outer = AMB if i == 0 else Z[i-1][2]
    print(f"  {n:<20}{w:>7.0f}'{t:>9.0f}C{t-AMB:>15.0f}C{t-outer:>16.0f}C")

# exposed envelope per linear foot: two side walls + roof (floor is ground-coupled)
nest_area = 2*H + Z[0][1]
vol = Z[0][1] * H
det_area = sum(2*H + (Z[0][1]/len(Z)) for _ in Z)
print(f"\n  conditioned volume            {vol:>8,.0f} cu ft / linear ft")
print(f"  exposed envelope, NESTED      {nest_area:>8,.0f} sq ft / linear ft")
print(f"  exposed envelope, DETACHED    {det_area:>8,.0f} sq ft / linear ft")
print(f"  ⭐ nesting cuts exposed area by {(1-nest_area/det_area)*100:.0f}%")

hot_det  = sum((t-AMB) for _, _, t in Z)
hot_nest = sum((t - (AMB if i==0 else Z[i-1][2])) for i,(_,_,t) in enumerate(Z))
print(f"  ⭐ and cuts the driving ΔT by    {(1-hot_nest/hot_det)*100:.0f}%"
      f"   ({hot_det:.0f}C of gradient -> {hot_nest:.0f}C)")
print(f"  ⭐⭐ COMBINED, heat loss falls ~{det_area*hot_det/(nest_area*hot_nest):.1f}x."
      f" Only the OUTER skin ever sees weather,")
print( "      and it is the COOLEST zone, so it sees the smallest gradient of all.")

print("\n" + "=" * 76); print("  ⭐⭐⭐ AND THE COLD PIPE MAKES THE WHOLE BUILDING A CONDENSER")
print("=" * 76)
# a jungle house transpires heavily; cold glazing condenses it back out
AC = 2.0                               # acres of jungle house per mile of corridor
TRANS = 0.25                           # inches of transpiration per day, dense canopy
gal_day = AC * 27_154 * TRANS
print(f"  {AC} acres of jungle canopy transpires    {gal_day:>10,.0f} gal/day/mile")
print(f"  on a 25-mile segment                    {gal_day*25:>10,.0f} gal/day")
print(f"                                          {gal_day*25*365/325_851:>10,.0f} AF/yr")
print("  ⭐ Cold-pipe glazing on the outer skin condenses that back out — dehumidification")
print("     with NO compressor, the same trick a Seawater Greenhouse uses in a desert.")
print("  ⭐⭐ So the envelope is not just insulation. It is a WATER RECOVERY DEVICE, and the")
print("     cold that runs it is the same cold already bought to cool the servers.")
print("\n  ⚠ HONEST: transpiration rate is crop- and canopy-dependent (0.1-0.4 in/day is the")
print("     spread) and recovery is never 100% — glazing temperature, air movement and")
print("     ventilation losses all take a cut. Treat as an order of magnitude, not a spec.")
