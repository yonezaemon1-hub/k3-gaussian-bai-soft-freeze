# Reproduction

The core result is checked with exact symbolic arithmetic in SymPy; no Monte
Carlo simulation, API call, GPU, or external dataset is required.

## Requirements

- Python 3.10 or later
- SymPy 1.14.0

## Cross-platform

```bash
python -m pip install -r requirements.txt
python src/verify_soft_freeze.py
```

A successful run ends with:

```text
PASS_EXACT_SYMBOLIC_AUDIT
C3 = 1/2 + sqrt(2)/2 = 1.20710678118655
NEW_UPPER = 75/61 = 1.22950819672131
OLD_U3 = 11/2 - 3*sqrt(2) = 1.25735931288071
IMPROVEMENT = 0.0278511161594034
BERNSTEIN_INTERVALS_PASS = 5/5
```

## Windows PowerShell

From the repository root:

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
.\scripts\VERIFY_FROM_POWERSHELL.ps1
```

The PowerShell gate checks that Python is available, confirms SymPy is 1.14.0,
runs the symbolic audit, and fails closed unless both PASS markers are present.

## What the audit checks

The exact script verifies:

1. the relation `(75/61) * (61/600) = 1/8`;
2. branch-rate comparison identities used to lower-bound the soft-freeze error exponent;
3. the cleared-denominator static-oracle polynomial identity;
4. two negative discriminants used in the positivity argument;
5. the quintic identity `4*c0*c2 - c1^2 = 4*q5`;
6. positive degree-5 Bernstein coefficients on five rational subintervals covering `[1/4, 2/3]`;
7. the reported lower endpoint, new upper endpoint, previous upper endpoint, and improvement.

Because the certificate uses exact rational arithmetic, the PASS result is not a floating-point tolerance check.
