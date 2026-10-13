# Theorem status

This register describes the current claims of the four canonical manuscripts. Compilation and executable checks are not independent peer review or formal verification.

## Paper I — heterogeneous four-state Potts broadcasting

**Established in the manuscript**

- For every locally finite deterministic rooted tree and edge parameters $0<\lambda_e\le q<1$, reconstruction is equivalent to positivity of the stated $L^3$ capacity with path weights given by products of squared edge eigenvalues.
- The result does not assume a uniform degree bound or a positive lower bound on the channel parameters.
- Positive capacity implies robust reconstruction after every fixed nonzero additional terminal Potts channel.
- Quadratic root posterior information is comparable, up to constants depending only on $q$, with capacity truncated at one.
- Without a uniform contraction bound, reconstruction implies positivity of an edge-weighted necessary capacity using the weight $1-\lambda_e^4$.
- On one ray, the weighted capacity criterion is exact.

**External mathematical input**

- The necessity direction under uniform contraction imports the preserved-class four-state posterior moment-saving inequality from the pinned OpenAI threshold preprint.
- The sufficiency direction and its robust version do not use that imported certificate theorem.

**Open in this repository**

- A full weighted-capacity converse for arbitrary trees when the channel parameters may approach one.
- Random-tree and block-model consequences are not claimed.

## Paper II — robust random $k$-SAT hitting-time variance

**Established in the manuscript**

- For each fixed $k\ge3$, independent, not necessarily identically distributed proper-clause streams satisfying fixed two-sided pointwise comparison with the uniform proper-clause law have variance $O(n)$ for the first unsatisfiable prefix.
- The same linear upper bound holds uniformly for every fixed linear clipping horizon.
- No temporal stationarity or regularity is assumed.
- A lower pointwise comparison alone does not force linear fluctuations: the manuscript gives an admissible lower-only example with uniformly bounded hitting-time second moment.

**Open in this repository**

- Whether the full two-sided comparison hypothesis forces a matching $\Omega(n)$ lower variance bound.
- Sub-Gaussian tails at scale $\sqrt n$ are not claimed.
- Extensions replacing global pointwise comparison by weaker local assumptions are suggested but not proved.

## Paper III — Brownian sampler observation-time stabilization

**Established in the manuscript**

- Conditional on the sampled configuration, the coordinate stabilization marks are independent and have law $4\chi_1^2$; hence the entire mark field is independent of the sampled configuration.
- Exact finite-set stabilization, defect-count, confidence-horizon, unequal-rate, and deterministic-clock formulas follow.
- The rescaled extreme stabilization point process converges to a Poisson point process with intensity $e^{-x}\,dx$, yielding the Gumbel maximum law.
- The finite-dimensional Gaussian observation model satisfies the stated entropy--MMSE identity and supplies a Bayes benchmark.

**Scope boundary**

- These random times measure observation time after the reconstructed path is available. They are not coding radii and do not prove that the OpenAI factor map is finitary.

## Paper IV — conjugate fibres, certificate rigidity, and irrationality exponents

**Established in the manuscript**

- If $e^{a\xi}=b$ is an algebraic exponential certificate with minimal certificate field $F=\mathbb Q(a,b)$ of degree $d$, then $\mu(\xi)\le2d$.
- If $F$ has the inversion involution $a\mapsto-a$, $b\mapsto b^{-1}$, then $\mu(\xi)\le d$. Equivalently, $\mu(\xi)\le2d/r$, where the compatible count $r$ is proved to lie in $\{1,2\}$.
- All algebraic exponential certificates for a fixed nonzero real $\xi$ have coefficients on one rational line.
- Every compatible embedding is either the identity or the unique inversion involution. In particular, the scalar compatible-fibre mechanism cannot produce three or more distinct compatible embeddings in the minimal field.
- Optimization over all scalar certificates reduces to powers of any one certificate. The resulting intrinsic complexity $\kappa_{\exp}(\xi)$ is a positive integer, is attained, and equals the eventual constant value along sufficiently divisible powers; $\mu(\xi)\le2\kappa_{\exp}(\xi)$.
- Scalar complexity one is classified by one-dimensional tori over $\mathbb Q$: split rational logarithms and quadratic norm-one tori, including the completed quadratic artanh/arctan family and its torsion boundary.
- For positive algebraic $\alpha\ne1$, the exact scalar complexity of $\log\alpha$ is the power degree $d_{\mathrm{pow}}(\alpha)$, giving $\mu(\log\alpha)\le2d_{\mathrm{pow}}(\alpha)$.
- Further applications include relative norm-one bounds, $\mu(\lambda\pi)\le[\mathbb Q(i/\lambda):\mathbb Q]$ for nonzero real algebraic $\lambda$, bounds for arguments of algebraic numbers, and $\operatorname{PGL}_2(\mathbb Q)$-invariance of irrationality exponent.
- The compatible-place proof jointly optimizes the rational-approximation and Taylor-collision penalties. It also proves the row first-moment asymptotic $\bar\beta_H=\frac{m}{m+2}\theta+O(H^{-1})$ and a finite-dimensional barrier showing that the resulting aggregate scalar estimate cannot cross the threshold $2d/r$.
- The compatible-place bound is uniform over all maximal minors, giving the corresponding analytic bound for every fixed norm of the full Plücker vector.

**External mathematical input and provenance**

- The determinant proof uses the bounded-fibre moving-centre interpolation theorem and the analytic row-translation/collision estimates of Liu–Jiang–Zhang, with the complex-centre and repeated-fibre transfer checked explicitly in the manuscript.
- Dan Brown independently proved the positive-rational logarithm theorem, formalized that theorem in Lean 4, and recorded the degree bound for logarithms of positive real algebraic numbers.
- Eric Naslund’s public posts of 9 and 12 October 2026 are credited as prior public identification of the quadratic exact-two family. The converse rigidity/classification and higher-degree bounds are claims of the present manuscript.
- Sean Litsey’s Catalan irrationality-measure paper is cited as contemporary methodological context for mixed-determinant perturbation and continuous defect optimization; the collision-energy lemma in Paper IV is derived directly from the Liu–Jiang–Zhang row-translation and collision inputs.

**Scope boundary and open strengthenings**

- The manuscript classifies the exact-two locus of the scalar certificate method; it does not classify all real numbers of irrationality exponent 2.
- It does not prove exponent 2 for every algebraic exponential fibre. The proposed algebraic exponential-fibre and algebraic linear-forms-in-logarithms statements remain conjectural.
- The threshold $2d/r$ is sharp for the optimized aggregate scalar estimate combining approximation and collision energy, not necessarily for the underlying constants. Improving it requires information not captured by that aggregate occupancy bound, such as detailed incidence, cancellation, finite-place structure, or non-scalar/full-Plücker arithmetic.
- The unitary-defect exact-two principle and effective special-centre interpolation statement are conjectural.
- The denominator threshold is qualitative because the imported moving-centre interpolation theorem has a centre-dependent Serre-vanishing threshold that is not made effective.
