# A 75/61 Upper Bound on the Universal Price of Three-Arm Gaussian Best-Arm Identification

Reproducibility repository for the preprint by **Ryutaro Yonezu** (Independent Researcher), dated August 30, 2026.

> **Status:** preprint / proof-audit candidate; not peer reviewed.

## DOI

Preprint: **10.5281/zenodo.22173805**  
Software / reproducibility package: **10.5281/zenodo.22173125**

## Main result

For fixed-budget best-arm identification with three unit-variance Gaussian arms, the manuscript gives the constructive universal-price bound

\[
P_3 \le \frac{75}{61} = 1.229508196721312\ldots
\]

The previously available explicit upper endpoint used in the manuscript is

\[
U_3 = \frac{11}{2}-3\sqrt{2} \approx 1.257359312880715,
\]

while the inherited lower endpoint is

\[
C_3 = \frac{1+\sqrt{2}}{2} \approx 1.207106781186547.
\]

Thus the explicit interval width is reduced from approximately `0.050252531694167` to `0.022401415534764`, a reduction of about **55.4%**.

## Soft-freeze policy

The constructive policy is deliberately simple:

1. Spend `14/25` of the total budget on a uniform pilot, i.e. `28/150` per arm.
2. Identify the arm with the smallest pilot empirical mean.
3. **Freeze additional sampling** of that pilot-worst arm.
4. Split the remaining `11/25` equally between the other two arms, i.e. `33/150` additional budget for each.
5. At the end, recommend the arm with the largest **cumulative empirical mean among all three arms**, including the frozen arm.

The key distinction is therefore between **sampling eligibility** and **final recommendation eligibility**: the frozen arm stops receiving samples but is not irreversibly eliminated from the decision set.

## Certified rate used in the proof

After normalizing the two gaps to `(1, r)` with `r >= 1`, the manuscript proves

\[
\Gamma_{SF}(r) \ge \min\{E_A(r),E_B\},
\]

where

\[
E_A(r)=\frac{7(89r^2-122r+122)}{8775},
\qquad
E_B=\frac{61}{600}.
\]

Combining this with the exact static-oracle comparison yields `P_3 <= 75/61`.

## Exact symbolic audit

The supplied SymPy audit checks the key rational identities, the static-oracle polynomial identity, two discriminants, the quintic identity, and strict positivity of all Bernstein coefficients on five rational subintervals.

### Quick reproduction

```bash
python -m pip install -r requirements.txt
python src/verify_soft_freeze.py
```

Expected status lines:

```text
PASS_EXACT_SYMBOLIC_AUDIT
BERNSTEIN_INTERVALS_PASS = 5/5
```

Reference numerical output:

```text
C3 = 1.20710678118655...
NEW_UPPER = 75/61 = 1.22950819672131...
OLD_U3 = 1.25735931288071...
IMPROVEMENT = 0.0278511161594034...
```

For Windows PowerShell, see `scripts/VERIFY_FROM_POWERSHELL.ps1` and `REPRODUCE.md`.

## Repository layout

- `paper/paper.tex` — LaTeX manuscript source
- `paper/paper.pdf` — compiled preprint
- `src/verify_soft_freeze.py` — exact SymPy proof audit
- `results/EXACT_SYMBOLIC_AUDIT.txt` — frozen reference audit output
- `docs/CLAIM_BOUNDARY.md` — explicit novelty / non-novelty boundary
- `scripts/VERIFY_FROM_POWERSHELL.ps1` — Windows reproduction gate
- `requirements.txt` — pinned Python dependency
- `CITATION.cff` — machine-readable citation metadata
- `SHA256SUMS.txt` — release integrity hashes

## Claim boundary

This repository **does not claim novelty** for two-stage BAI, pilot screening, adaptive allocation, elimination/screening in general, or the general idea that sampling eligibility and final recommendation eligibility may differ.

The narrow mathematical contribution claimed by the manuscript is the explicit guarantee

\[
P_3 \le 75/61
\]

for the stated three-arm unit-variance Gaussian fixed-budget policy, together with its exact symbolic certificate. See `docs/CLAIM_BOUNDARY.md`.

## Limitations

- The exact value of `P_3` is **not** determined.
- The construction is proved only for the stated **K=3, unit-variance Gaussian** setting.
- The fractions `14/25` and `11/25` are a rational proof-friendly design point, not claimed as universal constants.
- This repository has not been peer reviewed.

## License

Repository-authored software is released under the **MIT License**. The manuscript is licensed under **CC BY 4.0**. Third-party works cited by the manuscript remain under their respective licenses.

## Citation

Author: **Ryutaro Yonezu**, Independent Researcher.

Preprint DOI: **10.5281/zenodo.22173805**.

Software / reproducibility package DOI: **10.5281/zenodo.22173125**.

`CITATION.cff` records the software DOI at the package level and the preprint DOI in the preferred manuscript citation.
