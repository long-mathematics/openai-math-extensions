#!/usr/bin/env python3
"""Exact integer check for the coefficient count in Lemma 3.2.

Expands N_1 N_2 N_3 (1 - 2 s) in six formal variables without any
third-party symbolic-algebra dependency.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, Tuple

Monomial = Tuple[int, int, int, int, int, int]
Polynomial = Dict[Monomial, int]
ZERO: Monomial = (0, 0, 0, 0, 0, 0)


def monomial(index: int) -> Polynomial:
    exponent = [0] * 6
    exponent[index] = 1
    return {tuple(exponent): 1}  # type: ignore[arg-type]


def add(*polynomials: Polynomial) -> Polynomial:
    result: defaultdict[Monomial, int] = defaultdict(int)
    for polynomial in polynomials:
        for term, coefficient in polynomial.items():
            result[term] += coefficient
    return {term: coefficient for term, coefficient in result.items() if coefficient}


def scale(polynomial: Polynomial, scalar: int) -> Polynomial:
    return {term: scalar * coefficient for term, coefficient in polynomial.items()}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: defaultdict[Monomial, int] = defaultdict(int)
    for left_term, left_coefficient in left.items():
        for right_term, right_coefficient in right.items():
            term = tuple(a + b for a, b in zip(left_term, right_term))
            result[term] += left_coefficient * right_coefficient
    return {term: coefficient for term, coefficient in result.items() if coefficient}


def product(polynomials: Iterable[Polynomial]) -> Polynomial:
    result: Polynomial = {ZERO: 1}
    for polynomial in polynomials:
        result = multiply(result, polynomial)
    return result


def main() -> None:
    x = [monomial(i) for i in range(3)]
    y = [monomial(i + 3) for i in range(3)]

    r = [
        add(multiply(x[1], y[2]), multiply(x[2], y[1])),
        add(multiply(x[0], y[2]), multiply(x[2], y[0])),
        add(multiply(x[0], y[1]), multiply(x[1], y[0])),
    ]
    n = [add(x[i], y[i], r[i]) for i in range(3)]
    s = add(*(multiply(x[i], y[i]) for i in range(3)))
    expansion = multiply(product(n), add({ZERO: 1}, scale(s, -2)))

    total_l1 = 0
    pure_l1 = 0
    degree_one_l1 = 0
    surviving_mixed_l1 = 0
    pure_terms: list[tuple[Monomial, int]] = []

    for term, coefficient in expansion.items():
        absolute = abs(coefficient)
        degree_x = sum(term[:3])
        degree_y = sum(term[3:])
        total_l1 += absolute
        if degree_x == 0 or degree_y == 0:
            pure_l1 += absolute
            pure_terms.append((term, coefficient))
        elif degree_x == 1 or degree_y == 1:
            degree_one_l1 += absolute
        else:
            surviving_mixed_l1 += absolute

    expected_pure = {
        ((1, 1, 1, 0, 0, 0), 1),
        ((0, 0, 0, 1, 1, 1), 1),
    }
    assert set(pure_terms) == expected_pure
    assert total_l1 == 396
    assert pure_l1 == 2
    assert degree_one_l1 == 30
    assert surviving_mixed_l1 == 364
    assert pure_l1 + degree_one_l1 + surviving_mixed_l1 == total_l1

    print("exact expansion verified")
    print(f"monomials: {len(expansion)}")
    print(f"total coefficient L1 norm: {total_l1}")
    print(f"pure contribution: {pure_l1}")
    print(f"degree-one mixed contribution (vanishes): {degree_one_l1}")
    print(f"remaining mixed contribution: {surviving_mixed_l1}")
    print("third-moment constant: 364 + 12 = 376")


if __name__ == "__main__":
    main()
