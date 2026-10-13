# Dependency map

All OpenAI sources below are pinned to repository commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of `openai/math` rather than to the moving `main` branch.

## Paper I — heterogeneous four-state Potts broadcasting

Primary sources:

- OpenAI, [*The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/README.md) (October 5, 2026).
- OpenAI, [*A Capacity Criterion for Four-State Potts Reconstruction on Trees*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/README.md) (October 5, 2026).

Logical dependency:

- The necessity direction imports the preserved class of symmetric posterior laws and its moment-saving inequality from Proposition 3.2 of the threshold paper. The source proves the underlying polynomial inequalities by exact rational certificates.
- Closure is needed for arbitrary channel parameters and conditionally independent, nonidentical products; this was checked against the pinned source.
- The sufficiency direction, robust reconstruction corollary, local product identities, erasure argument, and path summation are proved in the Long manuscript and do not invoke that certificate theorem.
- The OpenAI capacity paper supplies the homogeneous bounded-degree comparison theorem being strengthened, not an additional logical hypothesis for the new proof.

## Paper II — robust random $k$-SAT hitting-time variance

Primary sources:

- OpenAI, [*Variance of the Random $k$-SAT Hitting Time*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/README.md) (September 27, 2026).
- OpenAI, [*Linear Variance of the Random 3-SAT Hitting Time*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/README.md) (October 5, 2026).

Logical/provenance role:

- The clause-omission/root-test framework and the critical occupation-potential idea originate in the OpenAI papers.
- The Long manuscript reproves the ingredients it uses in its nonuniform setting, including the general-$k$ one-clause comparison, robust potential drift, root-test bounds, occupation estimate, collision bounds, and cap removal. Thus the cited OpenAI results are provenance and comparison sources rather than black-box theorem assumptions in the final proof.

## Paper III — Brownian sampler observation-time stabilization

Primary source:

- OpenAI, [*The free uniform spanning forest is a factor of IID*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/README.md) (September 25, 2026).

Logical dependency:

- The Long manuscript takes as its sole sampler input the pinned source's complete reconstructed path-law representation for the Brownian sampler.
- After that representation, the stabilization law, independent marking, extreme-value point process, clock transforms, and finite-dimensional Bayes comparison are derived in the Long manuscript.
- The manuscript explicitly does not infer any coding-radius or finitary-factor property from the path-law input.

## Paper IV — conjugate fibres, certificate rigidity, and irrationality exponents

Primary OpenAI source:

- OpenAI, [*The irrationality exponent of π is 2*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md) (September 24, 2026).

Geometric and analytic input:

- Jingwen Liu, Kai Jiang, and Pingwen Zhang, [*Irrationality exponents of logarithms of positive rational numbers*](https://arxiv.org/abs/2610.10192), arXiv:2610.10192v2 (October 8, 2026).
- The Long manuscript imports their bounded-fibre moving-centre interpolation theorem and their row-translation/Taylor-collision estimates. It writes out the conjugated row identity and checks explicitly that the collision estimate is holomorphic in complex centres and does not require distinct multiplicative fibres.

Concurrent comparison source:

- Dan Brown, [*The irrationality measure of the logarithm of a rational number is 2*](https://jdb19937.github.io/log-irrationality-measure/logmeasure.pdf) (October 7, 2026), with [Lean 4 development](https://github.com/jdb19937/log-irrationality-measure).
- Brown independently proves the positive-rational logarithm theorem and formalizes that theorem in Lean. His Proposition 5.1 records the bound $\mu(\log\alpha)\le2[\mathbb Q(\alpha):\mathbb Q]$ for positive real algebraic $\alpha$.
- Brown's general-fibre interpolation theorem uses a global fibre-count condition. Liu–Jiang–Zhang's bounded-fibre theorem is the sharper input used here because its second volume condition depends on the maximum multiplicity within one multiplicative fibre.

Contemporary methodological comparison:

- Sean Litsey, [*An Irrationality Measure for Catalan's Constant*](https://hexagonmath.org/2610.00187v2), Hexagon 2610.00187v2 (October 2026).
- Litsey's mixed-determinant perturbation and missing-point energy estimates are cited as related context for retaining defect information continuously. Paper IV does not import these estimates as a black box: its collision-energy optimization is derived directly from the Liu–Jiang–Zhang row-translation and Taylor-collision bounds.

Public provenance for the quadratic exact-two family:

- Eric Naslund, public posts on X dated 9 and 12 October 2026; the later post linked the [public Claude discussion](https://claude.ai/share/ee870f04-b05b-4bf9-86fa-9d5f8d5bbd89).
- These posts are cited as prior public identification of the quadratic artanh family. They are not cited as sources for the converse rigidity, intrinsic saturation, higher-degree bounds, or determinant proof.

New logical content in Paper IV:

- Gelfond–Schneider is used to prove certificate-line rigidity and to show that every compatible embedding is the identity or a unique inversion involution. Thus the compatible count in a minimal certificate field is 1 or 2.
- The OpenAI/Liu–Jiang–Zhang determinant architecture is globalized over a number field by simultaneous denominator clearing, a product-formula lower bound, compatible-place analytic estimates, and crude estimates at incompatible embeddings.
- At compatible places the revised proof combines the linear rational-approximation cost and quadratic Taylor-collision energy in one convex optimization, proves the exact transverse row first moment, and obtains a finite-dimensional $2d/r$ barrier for this aggregate scalar architecture.
- The same compatible-place estimate is uniform over all maximal minors, yielding an analytic full-Plücker norm bound; the missing step in the conjectural full-Plücker route is arithmetic rather than analytic.
- The scalar theorem is reframed as $\mu(\xi)\le2d$, improved to $\mu(\xi)\le d$ under inversion; equivalently $\mu(\xi)\le2d/r$.
- Rigidity proves that arbitrary scalar-certificate optimization reduces to power saturation. The resulting integer complexity is attained and the complexity-one locus is classified by split and quadratic norm-one tori.
- The conjectural exponent-two theorem for every algebraic exponential fibre is not imported from any source and remains open in this repository.
