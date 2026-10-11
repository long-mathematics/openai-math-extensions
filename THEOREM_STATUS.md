# Theorem status

This register describes the current claims of the three canonical manuscripts. Compilation and executable checks are not independent peer review or formal verification.

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
