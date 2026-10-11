# Dependency map

All OpenAI sources below are pinned to repository commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of `openai/math` rather than to the moving `main` branch.

## Paper I — heterogeneous four-state Potts broadcasting

Primary sources:

- OpenAI, *The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model* (October 5, 2026).
- OpenAI, *A Capacity Criterion for Four-State Potts Reconstruction on Trees* (October 5, 2026).

Logical dependency:

- The necessity direction imports the preserved class of symmetric posterior laws and its moment-saving inequality from Proposition 3.2 of the threshold paper. The source proves the underlying polynomial inequalities by exact rational certificates.
- Closure is needed for arbitrary channel parameters and conditionally independent, nonidentical products; this was checked against the pinned source.
- The sufficiency direction, robust reconstruction corollary, local product identities, erasure argument, and path summation are proved in the Long manuscript and do not invoke that certificate theorem.
- The OpenAI capacity paper supplies the homogeneous bounded-degree comparison theorem being strengthened, not an additional logical hypothesis for the new proof.

## Paper II — robust random $k$-SAT hitting-time variance

Primary sources:

- OpenAI, *Variance of the Random $k$-SAT Hitting Time* (September 27, 2026).
- OpenAI, *Linear Variance of the Random 3-SAT Hitting Time* (October 5, 2026).

Logical/provenance role:

- The clause-omission/root-test framework and the critical occupation-potential idea originate in the OpenAI papers.
- The Long manuscript reproves the ingredients it uses in its nonuniform setting, including the general-$k$ one-clause comparison, robust potential drift, root-test bounds, occupation estimate, collision bounds, and cap removal. Thus the cited OpenAI results are provenance and comparison sources rather than black-box theorem assumptions in the final proof.

## Paper III — Brownian sampler observation-time stabilization

Primary source:

- OpenAI, *The free uniform spanning forest is a factor of IID* (September 25, 2026).

Logical dependency:

- The Long manuscript takes as its sole sampler input the pinned source's complete reconstructed path-law representation for the Brownian sampler.
- After that representation, the stabilization law, independent marking, extreme-value point process, clock transforms, and finite-dimensional Bayes comparison are derived in the Long manuscript.
- The manuscript explicitly does not infer any coding-radius or finitary-factor property from the path-law input.
