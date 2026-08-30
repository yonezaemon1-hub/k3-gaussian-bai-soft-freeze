# Claim boundary

## Claimed contribution

For the explicitly specified **three-arm, unit-variance Gaussian, fixed-budget**
soft-freeze policy in the accompanying manuscript, the work establishes the
constructive universal-price guarantee

`P_3 <= 75/61 = 1.229508196721312...`.

The proof is accompanied by an exact SymPy audit of the key algebraic
identities and the Bernstein-basis positivity certificate.

## Not claimed as novel

The work does **not** claim novelty for:

- two-stage best-arm identification;
- pilot screening;
- adaptive budget allocation;
- elimination or screening methods in general;
- ranking-and-selection / optimal computing budget allocation ideas in general;
- the broad principle of keeping an option eligible for final selection after
  stopping additional sampling;
- Gaussian large-deviation methods or convex quadratic projection methods in general.

## Scope limitations

The result does not determine the exact value of `P_3`. It does not establish
an analogous bound for `K > 3`, non-Gaussian rewards, unknown/unequal variances,
or other fixed-budget decision problems.

The fractions `14/25` and `11/25` are a rational design point chosen because it
admits a clean exact certificate. They are not claimed as universal constants.

## Review status

This is a preprint / proof-audit candidate and has not been peer reviewed.
