#!/usr/bin/env python3
"""Export the proved soft-freeze rate lower envelope as CSV.

This script visualizes formulas already proved in the manuscript. It is not a
Monte Carlo estimator and does not add a new theorem.
"""

import csv
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "certified_rate_curve.csv"


def e_a(r: Fraction) -> Fraction:
    return Fraction(7, 8775) * (89 * r * r - 122 * r + 122)


E_B = Fraction(61, 600)


def main() -> None:
    rows = []
    # r = 1.00, 1.01, ..., 4.00 using exact rationals.
    for i in range(100, 401):
        r = Fraction(i, 100)
        ea = e_a(r)
        certified = min(ea, E_B)
        rows.append((float(r), float(ea), float(E_B), float(certified), "E_A" if ea <= E_B else "E_B"))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["r", "E_A", "E_B", "certified_lower_envelope", "active_branch"])
        w.writerows(rows)

    assert e_a(Fraction(1, 1)) > 0
    assert E_B == Fraction(61, 600)
    print("PASS_CERTIFIED_RATE_CURVE_EXPORT")
    print(OUT)


if __name__ == "__main__":
    main()
