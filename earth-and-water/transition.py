#!/usr/bin/env python3
"""
transition.py — what it costs, per acre, to stop growing alfalfa and start growing something else.

    python3 transition.py            → the table
    python3 transition.py --sweep    → + the price sensitivity that decides tier Z

THE QUESTION, IN SUM'S WORDS: "the transition is what bankrupts every farmer. we pay them to
transform, X, back loans for the rest Y at 3% from federal funds or even local bonds."

So every number here is one of two kinds — a ONE-TIME COST TO CONVERT, and an ANNUAL NET AFTER
CONVERTING. The whole instrument lives in the gap between them. If the new annual net covers the
debt service on the loan half, the farmer is better off on day one and the state buys acre-feet
for the grant half only. If it does not, the bill is asking someone to go broke slowly instead of
quickly, and it should not pass.

⚠⚠ THE THING THIS MODEL KEEPS FINDING, and it is not what I expected going in:
    the water arithmetic and the money arithmetic point at DIFFERENT TIERS.
    X saves the most water and earns nothing.  Z earns the most and saves less than X.
    Y — the one everybody's grandfather actually did — barely saves any water at all.
    ⚠ IRRIGATED PASTURE USES MORE WATER THAN ALFALFA. Grazing it is the saving, not seeding it.

⚠ AND THE 2026 HAY PRICE MOVED AGAINST US. The Farm Bureau's "Alfalfa in the Red" number was
   −$203/acre at $171/ton (2025). Utah auction hay is $256/ton now — the national herd is at a
   74-year low and hay followed it up. At $256 alfalfa makes money again. THE ARGUMENT CANNOT
   REST ON THE CROP LOSING MONEY. It has to rest on the water, which is stable, or on the
   herd rebuild ending, which it will.

sources are named inline. every one of them is public and none of them is ours.
"""
import sys

AF_INCH = 1 / 12.0

# ─────────────────────────────────────────────────────────────────────────────
# 0 · THE BASELINE — one irrigated acre of Utah alfalfa, 2026
# ─────────────────────────────────────────────────────────────────────────────
ALFALFA = dict(
    yield_t=3.5,            # tons/acre — Utah Farm Bureau, flat for a decade
    price_t=256.0,          # $/ton — Utah auction average, Aug 2026 (allhay.com)
    price_t_2025=171.0,     # $/ton — USDA-NASS 2025 YTD, the number THE-CROP was written on
    cost_t=229.0,           # $/ton full economic cost — Utah Farm Bureau
    water_af=4.25,          # AF/acre applied
    depletion=0.80,         # fraction consumed; the rest returns to the system
)


def alfalfa_net(price_t):
    rev = ALFALFA["yield_t"] * price_t
    cost = ALFALFA["yield_t"] * ALFALFA["cost_t"]
    return rev, cost, rev - cost


# ─────────────────────────────────────────────────────────────────────────────
# 1 · THE THREE TIERS
#
# grant  — the part the state buys, because the state is the one getting the water
# loan   — the part that becomes a business, at 3%, because the farmer keeps the upside
# ─────────────────────────────────────────────────────────────────────────────

X = dict(
    name="X · dryland grass", short="X · dryland grass",
    blurb="retire the irrigation, seed a perennial dryland stand, keep it maintained. "
          "the cheapest acre-foot in the West and the one nobody wants to sell.",
    grant=dict(**{
        "terminate the alfalfa stand (herbicide + tillage)": 85,
        "seedbed prep":                                       50,
        "dryland perennial seed, 14 lb PLS "
        "(crested + Siberian wheatgrass, forage kochia, sainfoin)": 165,
        "drill seeding":                                      35,
        "year-one weed control":                              45,
        "⚠ reseed reserve — 1 acre in 4 fails to take":       60,
    }),
    loan={},
    # ⚠ two seasons of irrigation are needed TO GET THE STAND. the water saving starts in year 3,
    #    not year 1, and a bill that promises it in year 1 is lying.
    water_after=0.0,
    revenue=38.0,        # 0.4 AUM/acre dryland grazing @ ~$25/AUM. it is not a living.
    opcost=14.0,
)

Y = dict(
    name="Y · grass-finished beef", short="Y · grass-fed beef",
    blurb="keep the ground green, keep the herd, stop cutting hay and start rotating stock. "
          "the hundred-year tradition. the newer thing is the alfalfa.",
    grant=dict(**{
        "terminate + seedbed":                                110,
        "irrigated pasture mix, 22 lb/acre":                  175,
        "drill + roll":                                        45,
        "perimeter + 8-paddock cross fence, 232 ft/acre "
        "@ $1.60/ft high-tensile":                            371,
        "stock water — pipeline + trough per 5 acres":        500,
        "flood → wheel-line/K-line conversion "
        "(Utah AWOP scale, 50% cost-share basis)":           1500,
    }),
    loan=dict(**{
        "corrals, handling, shade, scales":                   250,
        "the herd — 1 cow-calf unit per 2.5 acres "
        "@ $4,000/head, 2026 record cattle market":          1600,
        "working capital, year one":                          300,
    }),
    # ⚠⚠ grazed pasture, deficit-irrigated to 4 inches of forage rather than cut to 2 feet of hay.
    #    IRRIGATED PASTURE CUT FOR HAY RUNS 5.0 AF — MORE THAN ALFALFA. the saving is the grazing.
    water_after=3.20,
    revenue=0.0,         # computed below from the carcass
    opcost=0.0,
)

Z = dict(
    name="Z · strawberries from the year 3000", short="Z · strawberries",
    blurb="hugelkultur mounds on contour, terraced faces, drip on every face, "
          "a solar canopy overhead somebody else pays for, and the mound itself as the "
          "climate battery.",
    grant=dict(**{
        "terminate + land forming to contour":                200,
        "woody core — chipped municipal green waste, "
        "free material, haul + place 300 cy/acre":           600,
        "mound forming + terracing":                        1800,
        "⭐ passive ground-coupled air tubes IN the mound "
        "(no fans, no chiller — see note)":                   900,
        "drip, filtration, header, fertigation":            2200,
        "bird + wind netting":                              1100,
    }),
    loan=dict(**{
        "plants, year one — 30,000/acre at 1.4× terrace "
        "factor @ $0.28":                                   8400,
        "beds + mulch, year one":                           1400,
        "share of the packing shed and forced-air cooler, "
        "amortised over a 40-acre co-op":                   3500,
    }),
    water_after=1.90,    # 22.8 acre-inches. CA coastal organic applies 27.5 (UC Davis 2024);
                         # the mound core and the canopy shade take ~17% off that.
    revenue=0.0,
    opcost=0.0,
)

# ⭐ WHAT IS NOT IN TIER Z, AND WHY IT IS THE MOST IMPORTANT LINE ON THE PAGE
#
# the solar canopy. elevated agrivoltaic structure runs $1.10–1.60/W installed (20–40% over
# fixed-tilt) and an acre at a farming-compatible ground-coverage ratio carries ~250 kW.
#
#       250 kW × $1.35/W  =  $337,500 PER ACRE
#
# ⚠⚠ that is SEVENTEEN TIMES the entire farmer-side conversion. it cannot be in the grant, it
#    cannot be in the loan, and it must never appear on a farmer's balance sheet. It is owned by
#    whoever wanted the interconnect anyway. THE FARMER RECEIVES SHADE AND A LEASE CHEQUE.
#    ⭐ Which is the ratchet again, one scale down: no developer shows up, the farm is still a
#    farm; a developer shows up, the shade arrives for free.
CANOPY_CAPEX_PER_ACRE = 337_500
CANOPY_LEASE = 1_000          # $/acre/yr. published dual-use range is $300–2,000.

# the same logic kills the other exotic line. a ground-to-air heat exchanger under greenhouse
# glass costs $4.25–7.14/sq ft installed — $185,000 to $311,000 for an open acre. ⭐ SO DO NOT BUY
# ONE. 300 cubic yards of earth per acre, four feet deep, IS the thermal mass a GAHT pays fans to
# reach. the mound is the climate battery. the $900 line above is corrugated tube and labour.
GAHT_PER_ACRE_LOW = 4.25 * 43_560
GAHT_PER_ACRE_HIGH = 7.14 * 43_560


# ─────────────────────────────────────────────────────────────────────────────
# 2 · WHAT EACH TIER EARNS
# ─────────────────────────────────────────────────────────────────────────────

def beef_per_acre(aum_per_acre=5.0, hang_price=5.90, cost_per_head=1900.0):
    """Irrigated pasture in good condition carries 5 AUM/acre (2.5 poor, 7+ excellent).

    A grass-finished steer takes ~14 AUM of forage to reach 1,150 lb live. Dressing 62% gives
    713 lb hanging. USDA's National Grass Fed Beef Report (Q2 2026) puts whole-carcass
    direct-to-consumer hanging weight at $5.90/lb — the customer pays the processor separately.
    """
    aum_per_head = 14.0
    head = aum_per_acre / aum_per_head
    hanging = 1150 * 0.62
    gross = head * hanging * hang_price
    return gross, head * cost_per_head, head


def berries_per_acre(trays=3500, price=16.0):
    """UC Davis 2024 organic, Central Coast: 7,000 trays @ $16 = $112,000 gross, and it nets
    $8,555. A 7.6% margin — HARVEST ALONE IS $65,727, or $9.39 a tray.

    ⚠ Utah is not Salinas. Shorter season, no coastal fog, day-neutral under a canopy. 3,500
    trays is half the California yield and the terrace factor is already in it. Halve the yield
    on a 7.6% margin and the acre is under water — which is the finding, not a rounding error.
    """
    harvest_per_tray = 65_727 / 7000
    cultural = 27_636 * 0.80          # less spray, less hand-weed under mulch and shade
    overhead = 6_330 - 3_200 + 300    # ⭐ CA land rent is $3,200/acre. Utah irrigated is ~$300.
    gross = trays * price
    cost = trays * harvest_per_tray + cultural + overhead
    return gross, cost


# ─────────────────────────────────────────────────────────────────────────────
# 3 · THE MONEY — patient capital against the alternative
# ─────────────────────────────────────────────────────────────────────────────
RATE_BILL = 0.03        # what §201 offers
RATE_MARKET = 0.08      # Farm Credit term paper, 2026
TERM = 20


def annuity(principal, rate, years):
    if rate == 0:
        return principal / years
    f = rate / (1 - (1 + rate) ** -years)
    return principal * f


def tot(d):
    return sum(d.values())


def run():
    W = 78
    print("=" * W)
    print("  DUSTY SPURS — the transition, per irrigated acre, Great Salt Lake basin")
    print("=" * W)

    rev26, cost26, net26 = alfalfa_net(ALFALFA["price_t"])
    rev25, _, net25 = alfalfa_net(ALFALFA["price_t_2025"])
    dep = ALFALFA["water_af"] * ALFALFA["depletion"]
    print(f"\n  BASELINE — alfalfa")
    print(f"    revenue  3.5 t × ${ALFALFA['price_t']:.0f}/t          ${rev26:>10,.0f}/acre")
    print(f"    cost     3.5 t × ${ALFALFA['cost_t']:.0f}/t           ${cost26:>10,.0f}/acre")
    print(f"    NET                              ${net26:>10,.0f}/acre   "
          f"(at 2025's $171/t: ${net25:,.0f})")
    print(f"    water    {ALFALFA['water_af']:.2f} AF applied, {dep:.2f} AF depleted")
    print(f"    water $/AF earned                ${rev26/ALFALFA['water_af']:>10,.0f}/AF")

    Y["revenue"], Y["opcost"], head = beef_per_acre()
    Z["revenue"], Z["opcost"] = berries_per_acre()

    rows = []
    for t in (X, Y, Z):
        g, l = tot(t["grant"]), tot(t["loan"])
        net = t["revenue"] - t["opcost"] + (CANOPY_LEASE if t is Z else 0)
        ds3 = annuity(l, RATE_BILL, TERM)
        ds8 = annuity(l, RATE_MARKET, TERM)
        saved = ALFALFA["water_af"] - t["water_after"]
        saved_dep = saved * ALFALFA["depletion"]
        rows.append(dict(t=t, g=g, l=l, net=net, ds3=ds3, ds8=ds8,
                         after=net - ds3, delta=net - ds3 - net26,
                         saved=saved, saved_dep=saved_dep,
                         per_af=(g / saved_dep) if saved_dep else float("inf")))

    for r in rows:
        t = r["t"]
        print("\n" + "─" * W)
        print(f"  {t['name'].upper()}")
        print(f"  {t['blurb']}")
        print("─" * W)
        print("    GRANT — the state buys the water")
        for k, v in t["grant"].items():
            print(f"      {k:<58} ${v:>7,.0f}")
        print(f"      {'':<58} ${r['g']:>7,.0f}  ← X")
        if t["loan"]:
            print("    LOAN — the farmer buys the business, 3% / 20 yr")
            for k, v in t["loan"].items():
                print(f"      {k:<58} ${v:>7,.0f}")
            print(f"      {'':<58} ${r['l']:>7,.0f}  ← Y")
        print(f"    TOTAL PER ACRE                                             "
              f"${r['g']+r['l']:>7,.0f}")
        print()
        print(f"    annual net, new use                     ${r['net']:>10,.0f}/acre/yr")
        print(f"    debt service @ 3%                       ${-r['ds3']:>10,.0f}")
        print(f"    ─────────────────────────────────────────────────────")
        print(f"    NET TO THE FARMER                       ${r['after']:>10,.0f}/acre/yr")
        print(f"    against alfalfa's ${net26:,.0f}                  "
              f"${r['delta']:>+10,.0f}/acre/yr")
        if t["loan"]:
            print(f"    ⭐ the 3% is worth                      "
                  f"${r['ds8']-r['ds3']:>+10,.0f}/acre/yr vs 8% paper")
        print(f"    water freed                             "
              f"{r['saved']:>10.2f} AF applied · {r['saved_dep']:.2f} depleted")
        print(f"    GRANT COST PER ACRE-FOOT DEPLETED       ${r['per_af']:>10,.0f}/AF  one time")

    # ── the line tier X cannot do without ───────────────────────────────────────────────────
    # capex alone leaves the dryland farmer $70/acre/yr WORSE off, so the grant buys nothing that
    # stays bought. The bill has to lease the freed water every year, instream, at a published
    # rate — which is also the only way the water is protected the whole way down to the lake.
    xr = rows[0]
    gap = net26 - xr["net"]
    breakeven = gap / xr["saved_dep"]
    lease = 30.0            # $/AF — the historic environmental-lease average in the West
    npv = xr["g"] + lease * xr["saved_dep"] * (1 - (1 + RATE_BILL) ** -TERM) / RATE_BILL
    print("\n" + "=" * W)
    print("  ⚠ TIER X DOES NOT CLOSE ON CAPEX — and the number that closes it is small")
    print("=" * W)
    print(f"    the gap against alfalfa                       ${gap:>10,.0f}/acre/yr")
    print(f"    break-even instream lease                     ${breakeven:>10,.2f}/AF/yr")
    print(f"    ⭐ the historic environmental lease average is ${lease:,.0f}/AF — ABOVE break-even.")
    print(f"    at ${lease:,.0f}/AF the dryland acre pays      "
          f"${xr['net'] + lease*xr['saved_dep'] - net26:>+10,.0f}/acre/yr vs alfalfa")
    print(f"    20-year NPV of grant + lease @ 3%             ${npv:>10,.0f}/acre")
    print(f"    ⭐ ALL-IN COST OF THE WATER                    "
          f"${npv/xr['saved_dep']:>10,.0f}/AF over 20 years")
    print(f"    against buying the right outright: $609–$25,000/AF (Utah range, THE-CROP)")

    print("\n" + "=" * W)
    print("  THE APPROPRIATION — what a round number buys")
    print("=" * W)
    print(f"  {'':<24}{'$/acre grant':>14}{'acres per $100M':>18}{'AF/yr freed':>15}")
    for r in rows:
        acres = 100_000_000 / r["g"]
        print(f"  {r['t']['short']:<24}${r['g']:>13,.0f}{acres:>18,.0f}"
              f"{acres*r['saved_dep']:>15,.0f}")

    deficit = 800_000
    print(f"\n  the lake's stated deficit: {deficit:,} AF/yr (GSL Strike Team)")
    for r in rows:
        if r["saved_dep"] <= 0:
            continue
        acres_needed = deficit / r["saved_dep"]
        print(f"    {r['t']['short']:<24} {acres_needed:>9,.0f} acres  "
              f"${acres_needed*r['g']/1e9:>6.2f} bn in grants")

    print(f"\n  ⚠ cattle-feed acreage in the basin is finite. USU puts basin cattle-feed water at")
    print(f"    908,729 AF/yr — {908_729/dep:,.0f} irrigated acres. That is the whole board.")
    print("  ⚠⚠ Y AND Z BOTH NEED MORE ACRES THAN EXIST. Only X closes the deficit on its own,")
    print("     and X is the tier nobody wants. So the bill is a BLEND, and the blend is the bill.")

    # ── THE BLEND ───────────────────────────────────────────────────────────────────────────
    board = 908_729 / dep
    slack = board * rows[0]["saved_dep"] - deficit      # AF spare if every acre went to X
    # ⚠ TIER Z IS CAPPED BY UTAH'S OWN APPETITE, NOT BY MONEY AND NOT BY WATER.
    #   3,500 trays × 8 lb = 28,000 lb/acre. Americans eat ~8 lb of strawberries a year.
    #   Utah is 3.5 million people. Do the division — it is a very small number of acres.
    z_cap = (3_500_000 * 8) / (3_500 * 8)
    z_ac = z_cap
    y_ac = (slack - z_ac * (rows[0]["saved_dep"] - rows[2]["saved_dep"])) / \
           (rows[0]["saved_dep"] - rows[1]["saved_dep"])
    x_ac = board - y_ac - z_ac
    mix = [(rows[0], x_ac), (rows[1], y_ac), (rows[2], z_ac)]
    grants = sum(r["g"] * a for r, a in mix)
    loans = sum(r["l"] * a for r, a in mix)
    annual = lease * x_ac * rows[0]["saved_dep"]

    print("\n" + "=" * W)
    print("  ⭐ THE BLEND — 800,000 AF/yr, inside the acreage that exists")
    print("=" * W)
    print(f"  ⚠ tier Z caps at {z_cap:,.0f} acres — that is EVERY STRAWBERRY UTAH EATS.")
    print(f"    California harvests 42,885. This is a garnish, not an industry.\n")
    print(f"  {'':<24}{'acres':>11}{'AF/yr':>12}{'grant $':>16}{'loan $':>16}")
    for r, a in mix:
        print(f"  {r['t']['short']:<24}{a:>11,.0f}{a*r['saved_dep']:>12,.0f}"
              f"{r['g']*a:>16,.0f}{r['l']*a:>16,.0f}")
    print(f"  {'':<24}{board:>11,.0f}{sum(a*r['saved_dep'] for r,a in mix):>12,.0f}"
          f"{grants:>16,.0f}{loans:>16,.0f}")
    print(f"\n    APPROPRIATION, one time                  ${grants/1e6:>10,.1f} M   grants")
    print(f"    REVOLVING LOAN FUND, 3%/20yr             ${loans/1e6:>10,.1f} M   returns")
    print(f"    INSTREAM LEASE, annual                   ${annual/1e6:>10,.1f} M/yr @ ${lease:,.0f}/AF")
    print(f"    ─────────────────────────────────────────────────────────")
    print(f"    ⭐ Utah has already appropriated $200 M to the Agricultural Water Optimization")
    print(f"       Program. As of Nov 2024, $48 M was obligated and $152 M WAS STILL SITTING")
    print(f"       THERE. The grant half of this bill is ${grants/1e6:,.0f} M.")
    print(f"\n  ⭐⭐ AND READ IT PER FARM, NOT PER ACRE — the politics live here.")
    keep = (y_ac + z_ac) / board
    print(f"     {keep*100:.0f}% of the ground stays irrigated and {100-keep*100:.0f}% goes to dry grass.")
    print(f"     Which is not {100-keep*100:.0f}% of farms closing. It is a 500-acre alfalfa outfit")
    print(f"     putting {500*keep:.0f} acres into grazed pasture and berries, drying the other"
          f" {500-500*keep:.0f},")
    print(f"     ⭐ and clearing ${(500*keep*rows[1]['after'] + lease*500*(1-keep)*rows[0]['saved_dep'] + 500*(1-keep)*rows[0]['net']):,.0f}/yr against alfalfa's"
          f" ${500*net26:,.0f} on all 500.")

    print("\n" + "=" * W)
    print("  ⚠ WHAT THE CANOPY AND THE CHILLER WOULD HAVE COST")
    print("=" * W)
    print(f"    agrivoltaic canopy, 250 kW/acre @ $1.35/W   ${CANOPY_CAPEX_PER_ACRE:>10,.0f}/acre")
    print(f"    ground-to-air heat exchanger, per open acre "
          f"${GAHT_PER_ACRE_LOW:>10,.0f} – ${GAHT_PER_ACRE_HIGH:,.0f}")
    print(f"    tier Z, farmer side, as designed            ${tot(Z['grant'])+tot(Z['loan']):>10,.0f}/acre")
    print("    ⭐ neither exotic line is bought. the canopy is leased from whoever wanted the")
    print("       interconnect; the mound is the climate battery. that is the entire trick.")


def sweep():
    print("\n" + "=" * 78)
    print("  ⚠⚠ THE SENSITIVITY THAT DECIDES TIER Z — it is the PRICE, not the water")
    print("=" * 78)
    print("  net $/acre/yr, before the canopy lease\n")
    print(f"  {'trays/ac':>9}" + "".join(f"{p:>11}" for p in (16, 20, 24, 28, 32)))
    print(f"  {'':>9}" + "".join(f"{'$'+str(p)+'/tray':>11}" for p in (16, 20, 24, 28, 32)))
    for trays in (2500, 3000, 3500, 4000, 5000, 7000):
        line = f"  {trays:>9,}"
        for price in (16, 20, 24, 28, 32):
            g, c = berries_per_acre(trays, price)
            line += f"{g-c:>11,.0f}"
        print(line)
    print("\n  $16/tray  = $2.00/lb, Salinas wholesale. it is what a shipper pays.")
    print("  $32/tray  = $4.00/lb, and a Utah farmers market clears $6–8.")
    print("\n  ⭐⭐ AT WHOLESALE THE ACRE LOSES MONEY AT EVERY UTAH YIELD. At local price it is the")
    print("     most profitable acre in the state. THE CROP DOES NOT HAVE TO LEAVE THE BASIN —")
    print("     which is the other bill's entire mechanism, arriving from the opposite side.")


if __name__ == "__main__":
    run()
    if "--sweep" in sys.argv:
        sweep()
