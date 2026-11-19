"""Exact one-sided randomization test for RQ2 and RQ3 using private workbook.
Run: python verify_one_sided_tests.py /path/to/Route_Memory_Google_Forms_Results.xlsx
"""
import sys
from itertools import combinations
import pandas as pd

if len(sys.argv) != 2:
    raise SystemExit('Usage: python verify_one_sided_tests.py path/to/raw_workbook.xlsx')
responses = pd.read_excel(sys.argv[1], sheet_name='Form Responses')
answers = pd.read_excel(sys.argv[1], sheet_name='Answer Key')
key = dict(zip(answers.iloc[:, 0].astype(str).str.strip(), answers.iloc[:, 1].astype(str).str.strip()))
assert len(responses) == 20
assert responses['Assigned navigation group'].value_counts().to_dict() == {'MAP': 10, 'TBT': 10}
for stem, n, label in [('D', 5, 'Direction Recall'), ('L', 10, 'Landmark Recognition')]:
    scores = sum((responses[f'{stem}{i} — {label}'].astype(str).str.strip() == key[f'{stem}{i}']).astype(int) for i in range(1, n + 1)) * (100 / n)
    vals = scores.to_numpy()
    is_map = responses['Assigned navigation group'].eq('MAP').to_numpy()
    observed = vals[is_map].mean() - vals[~is_map].mean()
    total = vals.sum()
    extreme = 0
    count = 0
    for ix in combinations(range(20), 10):
        perm_delta = (2 * vals[list(ix)].sum() - total) / 10
        extreme += int(perm_delta >= observed - 1e-9)
        count += 1
    print(f'{label}: MAP-TBT={observed:.1f} pp, exact one-sided p={extreme/count:.8f} ({extreme}/{count})')
