#!/usr/bin/env python3
"""model.py — the return model. Sum: "how is that even a line item? didn't we solve that?"

He is right and I had been flagging it instead of computing it, which is the second time this
morning. This is the fifty-year cash flow, built segment by segment, auditable, with every
assumption named at the top and changeable in one place.

⚠ WHAT IT IS: a simple, undiscounted-and-discounted deployment model on the INCREMENTAL structure —
   32 segments of 25 miles, each with its own pump station and data centre, each funding the next.
⚠ WHAT IT IS NOT: a financing model. No debt schedule, no coupon, no tax. Those change WHEN the
   equity gets paid, not WHETHER the asset earns. Named as an open item at the bottom.

usage:  python3 model.py            # base case
        python3 model.py --power 30 --water 0.80
"""
import argparse

# ── the assumptions, all of them, in one place ────────────────────────────────────────────────
A = dict(
    segments=32, seg_miles=25,
    cap_first=1_350_000_000,      # ⚠ segment one carries intake works AND terminus, no upstream
    cap_rest=850_000_000,         # 2..n extend existing plant
    build_yr_1=1,                 # segments completed in year 1
    build_accel=0.35,             # extra segments per year of accumulated revenue, capped below
    build_max=4,                  # physical limit: laying rate, permitting, crews
    af_total=1_000_000,
    cost_af=1171,                 # reconstructed delivered cost
    price_af=1639,                # 90% of SLC commercial summer ($1,821)
    mw_total=2326,                # sellable average generation at the 800 ft spec
    power_mwh=45.0,
    heat_twh_per_seg=0.64,        # waste heat sold at each segment's data centre
    heat_mwh=25.0,
    horizon=50, discount=0.07,
)


def run(a):
    n, per = a['segments'], 1.0 / a['segments']
    seg_rev = (a['mw_total'] * per * 8760 * a['power_mwh']
               + a['af_total'] * per * (a['price_af'] - a['cost_af'])
               + a['heat_twh_per_seg'] * 1e6 * a['heat_mwh'])
    rows, built, cum_cash, cum_rev, npv = [], 0, 0.0, 0.0, 0.0
    payback = payback_disc = None
    for yr in range(1, a['horizon'] + 1):
        # how many segments can we start this year — funded by accumulated operating margin
        want = a['build_yr_1'] if yr == 1 else min(a['build_max'],
                                                   a['build_yr_1'] + a['build_accel'] * (yr - 1))
        add = min(want, n - built)
        capex = 0.0
        for i in range(int(add)):
            capex += a['cap_first'] if built + i == 0 else a['cap_rest']
        frac = add - int(add)
        if frac:
            capex += frac * a['cap_rest']
        built += add
        rev = built * seg_rev                       # completed segments earn a full year
        net = rev - capex
        cum_cash += net
        cum_rev += rev
        npv += net / (1 + a['discount']) ** yr
        if payback is None and cum_cash > 0:
            payback = yr
        if payback_disc is None and npv > 0:
            payback_disc = yr
        rows.append((yr, built, capex, rev, cum_cash, npv))
    return rows, seg_rev, payback, payback_disc


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--power', type=float); p.add_argument('--water', type=float)
    p.add_argument('--quiet', action='store_true')
    g = p.parse_args()
    a = dict(A)
    if g.power: a['power_mwh'] = g.power
    if g.water: a['price_af'] = 1821 * g.water
    rows, seg_rev, pb, pbd = run(a)

    print(f"THE RETURN MODEL — {a['segments']} segments x {a['seg_miles']} mi, "
          f"power ${a['power_mwh']:.0f}/MWh, water ${a['price_af']:,.0f}/AF")
    print(f"  revenue per completed segment: ${seg_rev/1e6:,.0f} M/yr")
    print()
    if not g.quiet:
        print(f"{'yr':>4}{'built':>7}{'capex':>12}{'revenue':>11}{'cum cash':>13}{'NPV @7%':>13}")
        for yr, built, capex, rev, cum, npv in rows:
            if yr <= 20 or yr % 5 == 0:
                print(f"{yr:4d}{built:7.1f}{capex/1e6:11,.0f}M{rev/1e6:10,.0f}M"
                      f"{cum/1e9:12,.2f}B{npv/1e9:12,.2f}B")
    tot_cap = sum(r[2] for r in rows)
    print()
    print(f"  total capital deployed      ${tot_cap/1e9:,.2f} bn")
    print(f"  fully built in year         {next(r[0] for r in rows if r[1] >= a['segments']-0.01)}")
    print(f"  ⭐ SIMPLE PAYBACK            year {pb}")
    print(f"  ⭐ DISCOUNTED (7%) BREAK-EVEN year {pbd}")
    print(f"  cumulative cash @ year 50   ${rows[-1][4]/1e9:,.1f} bn")
    print(f"  NPV @ 7% over 50 years      ${rows[-1][5]/1e9:,.1f} bn")


if __name__ == '__main__':
    main()
