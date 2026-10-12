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

## Paper IV — conjugate fibres and irrationality exponents

Primary OpenAI source:

- OpenAI, [*The irrationality exponent of π is 2*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md) (September 24, 2026).

Additional geometric input:

- Jingwen Liu, Kai Jiang, and Pingwen Zhang, *Irrationality exponents of logarithms of positive rational numbers*, arXiv:2610.10192v2 (October 8, 2026).

Logical/provenance role:

- The manuscript extends the separated-weight interpolation-determinant method used in the OpenAI π paper from the single rational-valued fibre to algebraic exponential certificates with several compatible conjugate fibres.
- It imports the bounded-fibre moving-centre interpolation theorem and the row-translation/collision estimates from Liu--Jiang--Zhang, then adds simultaneous number-field denominator clearing and a product-formula comparison across embeddings.
- The resulting scalar norm argument proves the bound $2d/r$ and its certificate-optimization, power-saturation, torsion-defect, and relation-lattice corollaries. It does not claim the conjectural exponent-2 statement for every algebraic exponential fibre.
