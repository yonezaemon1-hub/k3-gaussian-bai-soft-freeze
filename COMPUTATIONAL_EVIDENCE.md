# Computational evidence backfill

Status: candidate for a future manuscript version; the currently published preprint is unchanged.

This paper already has unusually strong computational proof support: `src/verify_soft_freeze.py` performs exact symbolic checks and a five-interval Bernstein-positivity certificate. The backfill does not replace that certificate with Monte Carlo. Instead it makes the certified rate geometry directly plottable.

## Existing exact audit

```bash
python src/verify_soft_freeze.py
```

Expected core status:

```text
PASS_EXACT_SYMBOLIC_AUDIT
BERNSTEIN_INTERVALS_PASS = 5/5
```

## Added certified-rate curve

```bash
python scripts/export_certified_rate_curve.py
```

This writes `results/certified_rate_curve.csv`, sampling the proved lower envelope

`min(E_A(r), E_B)` for `r >= 1`, where

`E_A(r) = 7(89 r^2 - 122 r + 122) / 8775`

and `E_B = 61/600`.

The CSV is intended for a manuscript figure showing where the two certified branches exchange control. It is a visualization of proved formulas, not empirical evidence for an unproved rate.

## Claim discipline

The exact symbolic audit remains the primary computational certificate. The sampled curve does not determine the exact value of `P_3` and does not establish optimality of the proof-friendly pilot fraction `14/25`.
