from sympy import (
    Rational, symbols, sqrt, expand, factor, Poly, binomial, solve, discriminant, simplify, together
)

r, u, y, t = symbols('r u y t', real=True)
EA = Rational(7, 8775) * (89*r**2 - 122*r + 122)
EB = Rational(61, 600)
assert simplify(Rational(75,61)*EB - Rational(1,8)) == 0

# Branch formulas and key comparisons.
E02a = Rational(7,8775)*(122*r**2 - 122*r + 89)
E11 = Rational(7,8775)*(89*r**2 - 56*r + 89)
assert simplify((E02a - EA) - Rational(77,2925)*(r-1)*(r+1)) == 0
assert simplify((E11 - EA) - Rational(77,2925)*(2*r-1)) == 0
assert simplify(Rational(427,6675)*Rational(89,61)**2 - EB) == Rational(421,12200)
assert simplify((211*2**2-112*2+112)/Rational(1800) - EB) == Rational(61,200)
assert simplify(Rational(427,6675)*Rational(89,28)**2 - EB) == Rational(61,112)

# Static-oracle polynomial identity.
r_expr = 1 + u
x = (1-y)/2
f = y*(1-y)*(u**2 + 2*u + y)/(2*(u+y)*(u+2-y))
B = Rational(7,7137)*(89*r_expr**2 - 122*r_expr + 122)
P = expand(together(B-f) * 14274*(u+y)*(u+2-y))
P_expected = (
    1246*u**4 + 3276*u**3
    + (5891*y**2 - 4645*y + 2814)*u**2
    + (13490*y**2 - 12706*y + 2492)*u
    + 7137*y**3 - 8383*y**2 + 2492*y
)
assert expand(P-P_expected) == 0

c2 = 5891*y**2 - 4645*y + 2814
c1 = 13490*y**2 - 12706*y + 2492
c0_over_y = 7137*y**2 - 8383*y + 2492
assert discriminant(c2, y) == -44733071
assert discriminant(c0_over_y, y) == -866927

q5 = (
    42044067*y**5 - 128030643*y**4 + 159404895*y**3
    - 92334251*y**2 + 22844164*y - 1552516
)
assert expand(4*(y*c0_over_y)*c2 - c1**2 - 4*q5) == 0

# Power-to-Bernstein conversion by exact linear solve.
def bernstein_coeffs(poly, degree=5):
    b = symbols('b0:'+str(degree+1))
    basis = sum(b[i]*binomial(degree,i)*t**i*(1-t)**(degree-i) for i in range(degree+1))
    equations = Poly(expand(basis-poly), t).all_coeffs()
    sol = solve(equations, b, dict=True)[0]
    return [factor(sol[z]) for z in b]

intervals = [
    (Rational(1,4), Rational(1,2)),
    (Rational(1,2), Rational(13,24)),
    (Rational(13,24), Rational(9,16)),
    (Rational(9,16), Rational(7,12)),
    (Rational(7,12), Rational(2,3)),
]
expected_mins = [
    Rational(754465,32),
    Rational(2560325879,884736),
    Rational(725907743,393216),
    Rational(3111167339,1048576),
    Rational(286339193,27648),
]
for (a,b), expected in zip(intervals, expected_mins):
    poly = expand(q5.subs(y, a+(b-a)*t))
    coeffs = bernstein_coeffs(poly)
    assert all(c > 0 for c in coeffs)
    assert min(coeffs) == expected

C3 = (1+sqrt(2))/2
U3 = Rational(11,2)-3*sqrt(2)
new = Rational(75,61)
print('PASS_EXACT_SYMBOLIC_AUDIT')
print('C3 =', C3, '=', C3.evalf(15))
print('NEW_UPPER =', new, '=', new.evalf(15))
print('OLD_U3 =', U3, '=', U3.evalf(15))
print('IMPROVEMENT =', (U3-new).evalf(15))
print('BERNSTEIN_INTERVALS_PASS = 5/5')
