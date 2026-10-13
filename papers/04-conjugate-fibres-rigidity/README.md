# Paper IV — Conjugate Fibres, Certificate Rigidity, and Irrationality Exponents

[Read PDF](../../output/pdf/conjugate-fibres-rigidity.pdf) · [Canonical LaTeX](conjugate-fibres-rigidity.tex)

**Extends OpenAI:** [The irrationality exponent of π is 2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md).

**Moving-centre input:** [Liu–Jiang–Zhang, *Irrationality exponents of logarithms of positive rational numbers*](https://arxiv.org/abs/2610.10192). The manuscript also compares its logarithm bounds with [Dan Brown’s parallel paper and Lean development](https://github.com/jdb19937/log-irrationality-measure).

This is the canonical Paper IV source directory. For an algebraic exponential certificate $e^{ax}=b$ of degree $d$, the manuscript proves the bound $2d$, improved to $d$ when the unique inversion involution exists. Equivalently, it proves $2d/r$ and then shows by Gelfond–Schneider rigidity that the compatible count $r$ is always 1 or 2 in the minimal certificate field.

The rigidity theorem reduces optimization over all scalar certificates to power saturation of any one certificate. The resulting intrinsic complexity is a positive integer attained by a sufficiently divisible power. Complexity one is classified by the split torus and quadratic norm-one tori. Eric Naslund’s public quadratic artanh family is credited as prior identification of the forward complexity-one family; the paper’s contributions are the converse classification and the higher-degree bounds.

Applications include the power-degree bound for logarithms of positive algebraic numbers, relative norm-one bounds, and finite irrationality-exponent bounds for algebraic multiples of π and arguments of algebraic numbers. The paper does not prove exponent 2 for every algebraic exponential fibre.

See the repository-level [theorem status](../../THEOREM_STATUS.md) and [dependency map](../../DEPENDENCIES.md).
