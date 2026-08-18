BOOTS — PROPOSED AMENDMENTS v2
*12 August 2026. Three changes to BOOTS-BILL.md. Original untouched; this is the patch set.*

Existing section text is quoted from BOOTS-BILL.md. New text is marked NEW.
Numbering follows the original: 54-25-101 definitions, 201 water, 202 generation and
storage, 203 grid agreement, 301 severability.

---

# CHANGE 0 — THE CHAPTER IS TAKEN (verified against le.utah.gov, 12 Aug 2026)

## the collision
BOOTS enacts 54-25-101 through 54-25-301. **Title 54 Chapter 25 is already occupied** —
54-25-101 returns a live section on le.utah.gov. So are Chapters 26 and 27. The first
vacant chapter is **54-28**. (Checked by direct URL probe: 73-3-33, the section SPURS
enacts, IS vacant; every cross-reference in both bills — 65A-16-101, 65A-16-201,
54-17-601, 73-3-3, 73-10g-201 — exists as cited.)

Global fix: renumber every 54-25-* to 54-28-*, with a drafter's note that final numbering
is assigned by the Office of Legislative Research and General Counsel at introduction.

## the bigger finding inside the collision
**Title 54 Chapter 26 — "Large-Scale Electric Service Requirements" — is Utah's
existing large-load statute.** It governs contracts between qualified utilities and large
load customers (90-day negotiation period, separate accounting for large-scale service),
and the PSC has active rulemaking under it (Docket No. 25-R318-01, comment rounds through
October 2025).

Two consequences, one bad, one good:

**The overlap must be reconciled.** BOOTS §203 (mandatory grid support agreement with the
serving utility) and Chapter 26 (mandatory contract regime for large loads) would put the
same facility under two agreement frameworks. Options for counsel, in rough order of
cleanliness:
  (a) BOOTS's grid section becomes an amendment INTO Chapter 26 — a new part adding
      self-supply, storage and dispatch-for-compensation to the existing large-load
      framework — while the water and siting sections live in the new chapter;
  (b) BOOTS cross-references Chapter 26 and provides that an agreement under 203 may be
      combined with, or satisfied by, a Chapter 26 contract; or
  (c) facilities complying with BOOTS are expressly carved out of the Chapter 26 regime
      they no longer burden (they bring their own generation; the rationale for Chapter
      26's protections is cost-shifting to other ratepayers, which a self-supplied
      facility does not do).

**And the overlap is the sales pitch.** The legislature has already decided large loads
need their own statutory framework — that fight is over and won. BOOTS is not a novel
imposition on a new industry; it is the water-and-siting axle bolted onto a vehicle the
legislature already built and the PSC is actively tuning. Extension of live statute, not
invention — the same drafting posture as the CAMT hook in THE LEVER.

⚠ What Chapters 25 and 27 contain could not be read through the site's rendering — the
clinic should pull them first thing, both for the renumber and in case either one also
touches this subject matter.

---

# CHANGE 1 — 54-25-202, the storage safe harbour

## the problem
202(2) requires storage sufficient to serve peak load for 36 hours. 202(4) already says
any means qualifies and no technology is required. That is correct drafting and it is not
enough, because a legislative analyst with no instruction will price 36 hours in lithium —
about 3,600 MWh for a 100 MW facility, which is larger than the largest battery
installation on earth and reads as a de facto ban.

The requirement is not the error. The unpriced ambiguity is. Fix it by naming the field
without narrowing it.

## NEW — insert as 54-25-202(5), renumber existing (5) to (6)

        (5) A facility may satisfy Subsection (2) by any technology or combination of
technologies, including:
                (a) pumped hydroelectric storage, whether open loop or closed loop, and
whether at the surface or in existing underground workings;
                (b) gravitational storage using suspended mass;
                (c) compressed air storage, including storage in a solution-mined cavern;
                (d) thermal storage, including storage in rock, sand, water or molten salt;
                (e) hydrogen or another chemical carrier;
                (f) electrochemical storage, including a battery of any chemistry; or
                (g) any other means that delivers the capacity required by Subsection (2).
        This subsection is illustrative. Nothing in it requires, prefers, or excludes a
technology, and a technology absent from this list is not thereby disqualified.

## why this wording
- Batteries are named explicitly, at (f). A facility that wants to write a cheque for
  cells may do so. That was the point Sum raised: permit them, do not mandate them.
- Pumped storage is named first and includes underground workings, which is the Utah case.
- "Illustrative" and the final sentence prevent the list becoming a closed set.
- The cost note belongs in the explainer, not the statute. Statute stays boring.

---

# CHANGE 2 — NEW SECTION 54-25-204, below grade

## the problem this solves is political, not technical
BOOTS as drafted only takes. The Dusty Spurs page already names why that fails: *a bill
that only takes has nobody in the room arguing for it.* This section gives BOOTS a
constituency — every town that gets the surface back.

It is drafted as a condition of siting, not as an appropriation or a taking. Nobody's
property is taken; a facility that chooses to build here accepts the condition.

## NEW — 54-25-204. Surface use.

        (1) A thermal load facility commencing operation after the effective date of this
chapter shall place its heat rejection equipment and its computing or process equipment
below finished grade.
        (2) The surface estate above equipment placed under Subsection (1) shall remain
available for non-industrial use, and the use shall be determined by the land use
authority in which the facility is located.
        (3) A facility satisfies Subsection (2) by dedicating an easement, covenant or
other instrument of record that runs with the land and is enforceable by the land use
authority.
        (4) Subsection (2) does not require a facility to construct, fund, operate or
maintain a use selected under that subsection, and does not require public access to
security, electrical, mechanical or ventilation appurtenances.
        (5) A facility may retain at the surface only:
                (a) access, ventilation, electrical and emergency appurtenances;
                (b) generation and storage facilities permitted under Section 54-25-202;
and
                (c) an impoundment used for heat rejection or storage.
        (6) The land use authority may reduce or waive a requirement of this section for a
site where below-grade placement is infeasible by reason of groundwater, bedrock,
subsidence or flood hazard.
        (7) This section does not apply to a facility placed in service before the
effective date of this chapter.

## why this wording
- (2) hands the choice to the town, not the state and not the builder. Park, school,
  library, farm, housing, third place — the statute never names one, which is the same
  discipline as naming no crop in Dusty Spurs.
- (3) makes it recorded and enforceable rather than a promise.
- (4) is the concession that makes it passable: the facility owes the *space*, not a
  capital programme.
- (6) is the engineering escape hatch. Without it the bill is unbuildable on half the
  valley floor and someone will say so in committee.
- Below grade is already partly in the builder's interest: thermal mass, noise, viewshed,
  security. You are asking for something they half want.

---

# CHANGE 3 — 54-25-201, the internal collision

## the problem
201(1) prohibits consumptive heat rejection. 201(2) defines it as a process that evaporates
water withdrawn from within the basin and does not return it.

An open impoundment — the reference design in VEXI, and the thing that makes the seasonal
thermal loop work — evaporates. Read plainly, BOOTS bans its own reference design.

It is already survivable: 201(3) exempts a process that recovers and returns, and 201(4)
exempts water conveyed into the basin from outside it. **But nothing on the page says which
exemption the reference design is claiming, and a careful reader will conclude the drafter
did not read his own statute.**

## the fix is a clarifying subsection, not a change of policy

        NEW 54-25-201(8): An impoundment used for heat rejection or for energy storage is
not consumptive heat rejection under Subsection (1) to the extent it is filled and
replenished with water conveyed into the basin from outside it, or with water for which the
underlying right has been permanently retired from consumptive use within the basin.

## and the explainer must say this out loud
The reference design claims 201(4): **the pool is filled with imported water, or with water
bought once and retired.** Top-offs come from the same source. It is not claiming that
evaporation does not happen — it does, and it is a large part of how the pool sheds heat.

Say the number rather than the adjective. Open water in Utah loses roughly three to four
feet a year off the surface; a deep pool has far less surface per unit volume than a
shallow one; and the loss is metered by water balance, not estimated. That is the honest
version and it is stronger than "closed loop," which is not true of any open pond.

---

# THE EXPLAINER SECTION — "we can measure our loss"

*Drop-in copy for boots.html. Short on purpose.*

**Meter us.**

Water taken from a field is estimated. A coefficient, a crop model, a table — arguable
every year, in a dry year especially.

Water taken by this facility is measured. Metered in, metered out, and for the pond a water
balance from gauge, inflow, outflow and rainfall. The difference is what we did not give
back, and it is a number on a Tuesday, not an argument.

So charge us for it. Every acre-foot we consume, at the published rate, measured by
instruments already installed and open to the state engineer.

We are the easiest party in this basin to regulate honestly, and we would rather be first
than exempt.

*(A cooling tower throws away water every hot afternoon and calls it operations. We are
asking to be billed for less than that, and to prove it.)*

---

# WHAT I DID NOT CHANGE, AND WHY

**The 36 hours.** Sum's original instinct was right and my earlier objection was wrong —
I priced it in lithium. With pumped storage, duration is reservoir volume and volume is
cheap; the powerhouse is the expensive part. Keep 36. Arm it with Change 1 and a cost note
so nobody scores it in cells.

**The 150% generation.** It is doing double duty and should be left alone. The surplus is
what pumps the water, and it is the same ratio the corridor model needs.

**The 2035 retrofit date.** Politically the softest thing in the bill and the first thing an
existing operator will attack. Left as-is deliberately — that is a negotiating position, not
an oversight, and it should be traded away on purpose rather than pre-conceded.

**Section 203, the grid agreement.** Clean as written, including 203(4) — not a public
utility. That clause takes people a session to learn they needed.

# OPEN QUESTIONS FOR COUNSEL
1. Is 204 better as a state siting condition, or as an authorisation for local land use
   authorities to impose it? The second is weaker but nearly unopposable.
2. Does 204(2) need a duration? An easement in perpetuity versus the operating life of the
   facility are very different asks.
3. Does the 5 MW threshold in 101(6) sweep in large commercial HVAC, cold storage and food
   distribution? Hospitals and schools are exempt; the grocery warehouse is not.
4. Federal facilities within the basin — preemption. Worth an express carve-out rather than
   a fight.
