# Paper IV rigidity rewrite audit — 2026-10-13

## Scope

Paper IV was replaced and retitled **Conjugate Fibres, Certificate Rigidity, and Irrationality Exponents**. The old `04-conjugate-fibres-irrationality-exponents` source directory and PDF path are superseded by `04-conjugate-fibres-rigidity` and `conjugate-fibres-rigidity.pdf`.

## Mathematical changes

The replacement retains the number-field interpolation-determinant theorem but reorganizes and strengthens the paper around the following proved statements:

- certificate-line rigidity for all algebraic exponential certificates of one fixed real number;
- compatible-fibre rigidity: only the identity and a unique inversion involution can occur in the minimal certificate field;
- the equivalent bounds $2d$, or $d$ under inversion, rather than presenting an unrestricted compatible count before proving that the count is at most two;
- intrinsic power saturation and an attained positive-integer scalar complexity;
- classification of scalar complexity one by the split torus and quadratic norm-one tori;
- the exact scalar power-degree bound for logarithms of positive algebraic numbers;
- relative norm-one, algebraic-pi, algebraic-argument, and rational-projective consequences;
- explicit conjectural boundaries beyond the scalar method.

The compatible-place estimate now states why complex interpolation centres and repeated multiplicative fibres do not alter the Taylor-collision argument.

## Provenance and framing

- OpenAI’s pinned π preprint remains the foundational fixed-fibre result being extended.
- Liu–Jiang–Zhang is the black-box source for bounded-fibre moving-centre interpolation and the analytic determinant package.
- Dan Brown’s parallel rational-logarithm paper and Lean development are cited as concurrent work; the manuscript distinguishes the Lean-formalized rational theorem from Brown’s non-formalized algebraic degree bound.
- Eric Naslund’s public posts of 9 and 12 October 2026 are credited as prior public identification of the quadratic artanh family. The repository does not attribute the later converse rigidity, intrinsic saturation, or higher-degree bounds to those posts.
- The README and status files describe the quadratic exact-two family as prior provenance and the converse/higher-degree theory as the new contribution.

## Verification performed before the repository update

- The canonical source compiled with `latexmk`, Biber, and shell escape disabled.
- The resulting PDF has 21 pages.
- No unresolved citations, unresolved references, overfull boxes, or LaTeX errors were found.
- PDF metadata identifies Christopher D. Long as author and the strengthened title as document title.
- The root README uses only the repository-approved GitHub Markdown math syntax.
- The PDF and source hashes recorded in the manifest match the committed artifacts.

These checks establish artifact consistency and reproducibility. They are not independent peer review or formal verification of the new rigidity and number-field arguments.
