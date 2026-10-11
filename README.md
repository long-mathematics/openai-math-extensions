# OpenAI Math Extensions

This repository collects three independent extensions of recent OpenAI mathematical preprints. Each paper is self-contained after a precisely stated input from the corresponding source manuscript. The OpenAI sources are pinned to commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of `openai/math`.

## Papers

### Exact observation-time stabilization for the Brownian factor-of-IID sampler

The OpenAI Brownian sampler reconstructs a path field with the joint law

$$
Y_i(t)=tX_i+B_i(t).
$$

The paper determines the exact stabilization law of the midpoint decoder. Conditionally on the sampled configuration, the coordinate stabilization marks are independent with law $4\chi_1^2$. It also gives exact finite-set laws, Gumbel asymptotics, heterogeneous clocks, a vector I-MMSE entropy identity, and a Bayes snapshot benchmark. The stabilization parameter is observation time after path reconstruction; it is not a factor coding radius.

Source: [`papers/brownian-stabilization`](papers/brownian-stabilization)

### Robust variance bounds for random $k$-SAT hitting times

For fixed $k\ge 3$, the paper proves an $O(n)$ upper bound for the variance of the first unsatisfiable prefix in an independent, time-inhomogeneous stream of proper signed $k$-clauses whose laws are uniformly comparable with the uniform law. A stronger local criterion separates the actual inputs used by the proof: ordinary-clause drift, root-test density, root-incidence moments, and an assignment-falsification tail. No stationarity is required. A matching lower bound remains open in this generality.

Source: [`papers/robust-random-k-sat-variance`](papers/robust-random-k-sat-variance)

### A sharp capacity criterion for heterogeneous four-state Potts broadcasting

For arbitrary locally finite deterministic rooted trees and edge parameters $0<\lambda_e\le q<1$, reconstruction is equivalent to positivity of the associated $L^3$ nonlinear capacity with squared-channel path weights. The result removes the common-channel and bounded-degree assumptions, proves robust reconstruction, and gives two-sided comparison between quadratic root information and capacity. A weighted-capacity necessity theorem remains valid without uniform contraction and is exact on one ray.

Source: [`papers/heterogeneous-potts-capacity`](papers/heterogeneous-potts-capacity)

## Verification

Each paper is compiled from `main.tex`. The Potts source includes an exact symbolic expansion check:

```bash
python papers/heterogeneous-potts-capacity/verify_local_expansion.py
```

The GitHub workflow compiles all three manuscripts and runs this verifier.
