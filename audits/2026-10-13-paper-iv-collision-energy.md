# Paper IV collision-energy revision audit — 2026-10-13

## Scope

Paper IV retains its title, canonical source path, and headline theorems. This revision replaces the compatible-place low/high transverse-index dichotomy by a joint convex optimization of the rational-approximation penalty and the Taylor-collision energy.

The canonical paths remain:

- `papers/04-conjugate-fibres-rigidity/conjugate-fibres-rigidity.tex`
- `papers/04-conjugate-fibres-rigidity/references.bib`
- `output/pdf/conjugate-fibres-rigidity.pdf`

No temporary or revision-labelled manuscript filename is introduced.

## Mathematical changes

The revised proof:

- replaces the hard cutoff parameters (A,\eta,L) and the two-branch compatible-place argument by a single collision-energy inequality obtained by completing the square;
- keeps the finite-(H) lattice correction (S/H) in the optimized estimate;
- reduces the auxiliary parameter scheme to (	heta=\chi^2), (C=\chi^{-1}), and (	heta<B<\chi), with the single gap condition (r\nu(B-\theta)>d(1-\theta));
- proves the row first-moment asymptotic
  [
  \bar\beta_H=\frac{m}{m+2}\theta+O(H^{-1}),
  ]
  and records the associated Beta((m,2)) limiting distribution;
- identifies the near-extremal water-filling occupancy profile and records robustness under subexponential deterioration of the collision coefficient;
- proves a finite-dimensional barrier showing that the optimized aggregate approximation-plus-collision estimate cannot cross (2d/r);
- extends the compatible-place analytic estimate uniformly to the full vector of maximal minors, giving a fixed-(\ell^p) full-Plücker norm bound;
- sharpens the discussion of what would be required to improve the scalar threshold: detailed incidence, determinant cancellation, finite-place information, or non-scalar/full-Plücker arithmetic.

The headline theorem (mu(\xi)\le 2d/r), the rigidity theorem, power saturation, the complexity-one classification, and the downstream applications are unchanged.

## Further directions added

The revision records two additional conjectural directions:

- a unitary-defect exact-two principle extending the proved torsion-defect criterion;
- effective interpolation for the special centres (y_j=b^j), (c_{ji}=ja x_i).

The full-Plücker discussion is also sharpened: the analytic simultaneous-smallness estimate is now proved, leaving the adelic/projective arithmetic mechanism as the main missing step.

## Provenance

The imported geometric and analytic inputs remain the bounded-fibre moving-centre interpolation theorem and row-translation/Taylor-collision estimates of Liu–Jiang–Zhang.

Sean Litsey's *An Irrationality Measure for Catalan's Constant*, Hexagon 2610.00187v2, is added as contemporary methodological context for mixed-determinant perturbation and continuous defect optimization. The collision-energy lemma in Paper IV is not imported from Litsey; it is derived directly from the Liu–Jiang–Zhang estimates.

Existing provenance concerning OpenAI, Dan Brown, and Eric Naslund is unchanged.

## Verification

Before repository replacement, the revised canonical source and merged bibliography were built locally using the repository's LaTeX toolchain conventions, including Biber and shell escape disabled. The build had:

- 26 pages;
- no unresolved citations or references;
- no overfull boxes;
- source digest (using the repository's `source_digest` convention) `9516dab683426d9cb83fa6e5b2928d5153d69e7e78c56d0d13b911ba9cc82ceb`.

The pull-request regeneration pass completed successfully in the repository's Ubuntu workflow. It produced the canonical 26-page PDF with manifest hash `f7cceee00d3d1e809f309edf0d4a88597edeaf92e219cf60e84182446811e0bc`; repository tests, exact symbolic verification, and `make check` all passed in that run. The temporary patch/build scaffolding was removed and the standard workflow file was restored before final review.

These checks establish artifact consistency and reproducibility. They are not independent peer review or formal verification of the mathematical arguments.
