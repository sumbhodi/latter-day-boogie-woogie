#!/usr/bin/env bash
# sync-bills.sh — bills.html holds a COPY of the instrument text from dust/dusty/boots.
# Edit a bill on its own page, then run this. It re-extracts all three and reports drift.
# ⚠ The duplication is deliberate (counsel gets one page, no build step) but it CAN rot,
#   and a rotted copy of a statute is exactly what cost us the night of 17 Aug.
cd "$(dirname "$0")"
python3 - <<'PY'
import re
b = open('bills.html').read()
bad = 0
for f in ('dust.html','dusty.html','boots.html'):
    src = re.search(r'<div class="bill"><pre>(.*?)</pre>', open(f).read(), re.S).group(1).strip('\n')
    if src in b:
        print('  match  ' + f)
    else:
        print('  DRIFT  ' + f + '  → bills.html is stale for this bill'); bad = 1
raise SystemExit(bad)
PY
