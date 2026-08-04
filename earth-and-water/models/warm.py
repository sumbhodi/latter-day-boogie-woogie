#!/usr/bin/env python3
"""warm.py — Sum: "so flow is now captured temporarily as heat, as long as we want on a hill...
can we apply this to heat pumps and cool people too?"

Yes. And it closes THE-PIPE's loop: district energy only works in a dense LINEAR settlement,
which is the one geometry the corridor was already going to be.
"""
IT, PUE, HRS = 100, 1.10, 8760
HEAT_MWH = IT * PUE * HRS            # essentially all facility draw becomes heat
HOME_HEAT, HOME_COOL = 14.6, 9.0     # MWh thermal / home / yr  (US avg heat, desert cool)

print("=" * 74); print(f"  ONE {IT} MW NODE — the heat it is currently throwing away"); print("=" * 74)
print(f"  facility draw @ PUE {PUE}          {IT*PUE:>10,.0f} MW")
print(f"  heat rejected per year           {HEAT_MWH:>10,.0f} MWh  ({HEAT_MWH/1e6:.2f} TWh)")
print(f"\n  homes HEATED if none is wasted   {HEAT_MWH/HOME_HEAT:>10,.0f}")
print(f"  ⚠ but heating is SEASONAL — realistically 35% lands without storage:")
print(f"    homes heated, no storage       {HEAT_MWH*0.35/HOME_HEAT:>10,.0f}")
print(f"  ⭐ with seasonal pit/aquifer storage in the collection pool (Denmark does this")
print(f"     at 200,000 m3), you recover most of the rest.")

print("\n" + "=" * 74); print("  COOLING — and this needs no heat pump at all"); print("=" * 74)
print(f"  the cold pipe cools by HEAT EXCHANGER, not by a compressor.")
print(f"  homes COOLED per node (thermal)  {HEAT_MWH/HOME_COOL:>10,.0f}   ⚠ capacity, not demand")
print(f"  ⭐ in a desert this is a LIFE-SAFETY asset, not an amenity. Heat kills more")
print(f"     Americans than any other weather event.")

print("\n" + "=" * 74); print("  THE HEAT-PUMP MULTIPLIER — why the loop beats air"); print("=" * 74)
print(f"  {'source':<34}{'COP heat':>10}{'COP cool':>10}{'kWh/home/yr':>14}")
for tag, ch, cc in [("air-source, 105F desert summer", 3.0, 2.6),
                    ("ground-source (typical)",        4.2, 4.5),
                    ("OUR WATER LOOP",                 5.2, 6.0)]:
    e = HOME_HEAT*1000/ch + HOME_COOL*1000/cc
    print(f"  {tag:<34}{ch:>10.1f}{cc:>10.1f}{e:>14,.0f}")
air = HOME_HEAT*1000/3.0 + HOME_COOL*1000/2.6
ours= HOME_HEAT*1000/5.2 + HOME_COOL*1000/6.0
print(f"\n  ⭐ {(1-ours/air)*100:.0f}% less electricity per home than air-source.")
print(f"     at $0.14/kWh that is ${(air-ours)*0.14:,.0f}/home/yr — and it is the SAME PIPE")
print(f"     that cools the servers, so the capital is already spent.")

print("\n" + "=" * 74); print("  ⚠ THE CONSTRAINT THAT IS ACTUALLY THE DESIGN"); print("=" * 74)
print("  Heat does not travel. Insulated district mains lose economics past ~20-30 km, which")
print("  is why district energy fails in sprawl and works in dense linear settlement.")
print("  ⭐⭐ THE CORRIDOR IS A DENSE LINEAR SETTLEMENT. 25-mile segments = 40 km, each with")
print("     its own node at the pump station. District energy's hardest constraint is the")
print("     corridor's default geometry. THE-PIPE already drew this and did not know why.")

print("\n" + "=" * 74)
print("  SELL THE WATER, OR SELL THE COOL? — Sum's two product models")
print("=" * 74)
HOMES = 23_100      # heated per node without seasonal storage
TH_HOME = 23.6      # MWh thermal/home/yr (14.6 heat + 9.0 cool)
AIR_KWH, ELEC = 8_328, 0.14
their_cost = AIR_KWH * ELEC
print(f"  what a home spends today on air-source HVAC   ${their_cost:>8,.0f}/yr")
for disc in (0.25, 0.33, 0.50):
    px = their_cost * (1 - disc)
    print(f"    sell thermal at {disc:.0%} below that        ${px:>8,.0f}/yr"
          f"  ->  ${px*HOMES/1e6:>6,.1f} M/yr per node")
px = their_cost * 0.67
print(f"\n  ⭐ MODEL B (the pipe) at a 33% saving to the customer: "
      f"${px*HOMES/1e6:,.1f} M/yr")
print(f"  ⚠ MODEL A (the jug) on the same node:              $0.3 M/yr")
print(f"  ⭐⭐ THE SERVICE IS ~{px*HOMES/344_045:,.0f}x THE PRODUCT.")
print("\n  and the reason is not price, it is that Model B never sells the molecule:")
print("    · water goes out cold, comes back warm, never leaves our custody")
print("    · never an export -> never a Sporhase question, never a compact question")
print("    · the warm return is the INPUT to the next rung of the heat ladder")
print("    · contracted thermal revenue prices at 10-12x EBITDA. Trucking prices at 5x.")
print("\n  ⚠ ONE ENGINEERING CORRECTION: you do not reverse the FLOW twice a year.")
print("     In an ambient (5th-gen) loop the main circulates one way all year and each")
print("     building's own heat pump decides whether to EXTRACT or INJECT. No reversing")
print("     valves, no re-priming. ⭐ And when a data centre injects while housing extracts,")
print("     they trade heat through the loop and the NET DRAW IS NEAR ZERO.")
print("     What genuinely reverses twice a year is the STORE: charge in summer, spend in winter.")
