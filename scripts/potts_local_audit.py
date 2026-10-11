#!/usr/bin/env python3
"""Exact symbolic checks for the local algebra in Paper I."""

import sympy as sp

x1, x2, x3, y1, y2, y3 = sp.symbols("x1 x2 x3 y1 y2 y3")
u, v, tau1, tau2 = sp.symbols("u v tau1 tau2")
xs = (x1, x2, x3)
ys = (y1, y2, y3)
s = sum(a * b for a, b in zip(xs, ys))
R = (
    x2 * y3 + x3 * y2,
    x1 * y3 + x3 * y1,
    x1 * y2 + x2 * y1,
)
N = tuple(xs[i] + ys[i] + R[i] for i in range(3))

def symmetric_moment(exponents, second, third):
    degree = sum(exponents)
    if degree == 0:
        return sp.Integer(1)
    if degree == 1:
        return sp.Integer(0)
    if degree == 2:
        return second / 3 if sorted(exponents) == [0, 0, 2] else sp.Integer(0)
    if degree == 3:
        return third if exponents == (1, 1, 1) else sp.Integer(0)
    raise ValueError(exponents)

def expected(poly):
    polynomial = sp.Poly(sp.expand(poly), *xs, *ys)
    total = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        total += coefficient * symmetric_moment(powers[:3], u, tau1) * symmetric_moment(powers[3:], v, tau2)
    return sp.expand(total)

assert sp.simplify(expected(sum(r * r for r in R)) - sp.Rational(2, 3) * u * v) == 0
assert sp.simplify(expected(s * s) - sp.Rational(1, 3) * u * v) == 0
assert sp.simplify(expected(s * sum(xs[i] * R[i] for i in range(3))) - 2 * tau1 * v) == 0
assert sp.simplify(expected(s * sum(ys[i] * R[i] for i in range(3))) - 2 * u * tau2) == 0
assert sp.simplify(expected(s * sum(r * r for r in R)) - 6 * tau1 * tau2) == 0

third_polynomial = sp.Poly(sp.expand(N[0] * N[1] * N[2] * (1 - 2 * s)), *xs, *ys)
absolute_coefficient_sum = sum(abs(int(coefficient)) for _, coefficient in third_polynomial.terms())
assert absolute_coefficient_sum <= 448

print("Paper I local symbolic checks passed.")
print("Absolute coefficient sum:", absolute_coefficient_sum)
