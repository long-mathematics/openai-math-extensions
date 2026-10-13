# OpenAI Math Extensions

Four independent research manuscripts by **Christopher D. Long** extending recent OpenAI mathematical preprints. The papers share provenance rather than a single mathematical subject. OpenAI source dependencies are pinned to commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of `openai/math`.

## Read the papers

| Paper | Manuscript | PDF | LaTeX |
| --- | --- | --- | --- |
| **I** | **A Sharp Capacity Criterion for Heterogeneous Four-State Potts Broadcasting on Trees** | [Read PDF](output/pdf/heterogeneous-potts-capacity.pdf) | [Source](papers/01-heterogeneous-potts-capacity/heterogeneous-potts-capacity.tex) |
| **II** | **A Robust Linear Upper Bound for the Variance of Random $k$-SAT Hitting Times** | [Read PDF](output/pdf/robust-random-k-sat-variance.pdf) | [Source](papers/02-robust-random-k-sat-variance/robust-random-k-sat-variance.tex) |
| **III** | **Exact Observation-Time Stabilization Laws for the Brownian Factor-of-IID Sampler** | [Read PDF](output/pdf/brownian-sampler-stabilization.pdf) | [Source](papers/03-brownian-sampler-stabilization/brownian-sampler-stabilization.tex) |
| **IV** | **Conjugate Fibres, Certificate Rigidity, and Irrationality Exponents** | [Read PDF](output/pdf/conjugate-fibres-rigidity.pdf) | [Source](papers/04-conjugate-fibres-rigidity/conjugate-fibres-rigidity.tex) |

The PDFs are committed snapshots compiled from the linked canonical sources. Intermediate LaTeX files are kept out of the repository. The numbering gives these manuscripts stable identities inside this repository; it is not a logical dependency order.

## Paper guide

### Paper I — Heterogeneous four-state Potts capacity

[Read PDF](output/pdf/heterogeneous-potts-capacity.pdf) · [LaTeX](papers/01-heterogeneous-potts-capacity/heterogeneous-potts-capacity.tex)

Extends OpenAI: [The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/README.md) and [A Capacity Criterion for Four-State Potts Reconstruction on Trees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/README.md).

For edge-dependent four-state Potts channels satisfying a common strict upper contraction bound, reconstruction on every locally finite deterministic rooted tree is equivalent to positivity of the associated $L^3$ nonlinear capacity. The manuscript removes the bounded-degree and homogeneous-channel assumptions, proves robust reconstruction under every fixed nonzero terminal channel, and obtains two-sided comparison between capacity and quadratic posterior information.

Without a uniform contraction bound, it proves an edge-weighted necessary capacity statement with weight $1-\lambda_e^4$ and shows that this weighted criterion is exact on one ray. The full weighted converse on arbitrary trees remains open.

### Paper II — Robust random $k$-SAT hitting-time variance

[Read PDF](output/pdf/robust-random-k-sat-variance.pdf) · [LaTeX](papers/02-robust-random-k-sat-variance/robust-random-k-sat-variance.tex)

Extends OpenAI: [Variance of the Random k-SAT Hitting Time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/README.md) and [Linear Variance of the Random 3-SAT Hitting Time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/README.md).

For every fixed $k\ge 3$, independent proper-clause streams whose time-dependent laws are uniformly comparable with the uniform proper-clause law satisfy a uniform $O(n)$ upper bound for the variance of the first unsatisfiable prefix. The proof allows arbitrary deterministic time dependence and isolates the distinct roles of conditional-density comparison, root-incidence control, and the lower survival bound.

The manuscript does not claim a matching lower bound under the full two-sided comparison hypothesis. It also records why the available second-moment deletion argument does not by itself yield sub-Gaussian tails.

### Paper III — Brownian sampler stabilization

[Read PDF](output/pdf/brownian-sampler-stabilization.pdf) · [LaTeX](papers/03-brownian-sampler-stabilization/brownian-sampler-stabilization.tex)

Extends OpenAI: [The free uniform spanning forest is a factor of IID](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/README.md).

For the natural midpoint readout of the OpenAI Brownian sampler, the coordinate stabilization marks are independent with common law $4\chi_1^2$ and are independent of the sampled binary configuration. The manuscript derives exact finite-set and defect-count laws, an extremal Poisson point-process limit, unequal-rate and deterministic-clock formulas, and an entropy--MMSE comparison with the full Bayes decoder.

These are observation-time statements after the reconstructed path has been formed. They are not finitary-factor or coding-radius statements.

### Paper IV — Conjugate fibres, certificate rigidity, and irrationality exponents

[Read PDF](output/pdf/conjugate-fibres-rigidity.pdf) · [LaTeX](papers/04-conjugate-fibres-rigidity/conjugate-fibres-rigidity.tex)

Extends OpenAI: [The irrationality exponent of π is 2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md).

For an algebraic exponential certificate $e^{ax}=b$ of degree $d$, the manuscript proves an irrationality-exponent bound of $2d$, improved to $d$ when the unique inversion involution exists. The equivalent compatible-fibre form is $2d/r$, and a rigidity theorem shows that the minimal-field compatible count $r$ is always 1 or 2.

All scalar certificates for a fixed real number lie on one rational line. Consequently, optimization reduces to power saturation of any one certificate and produces an attained positive-integer complexity. Complexity one is classified by split rational logarithms and quadratic norm-one tori.

Further consequences include the power-degree bound for logarithms of positive algebraic numbers, relative norm-one estimates, and finite bounds for algebraic multiples of π and arguments of algebraic numbers. The paper does not claim exponent 2 for every algebraic exponential fibre.

## Status and provenance

- [Theorem status](THEOREM_STATUS.md) records proved statements, scope boundaries, and open strengthenings.
- [Dependency map](DEPENDENCIES.md) identifies the exact OpenAI inputs and which directions use them.
- [Initial audit](audits/2026-10-11-initial-audit.md) records the first repository-level audit and repair pass.

Compilation, exact symbolic checks, and finite computations check the written artifacts; they are not independent peer review or formal verification.

## Build and verification

On Debian/Ubuntu:

```sh
sudo apt-get install latexmk biber texlive-bibtex-extra texlive-latex-extra texlive-fonts-recommended texlive-science lmodern poppler-utils python3 python3-sympy make
```

From the repository root:

```sh
make pdf
make check
make test
make verify
```

Canonical manuscript entry points use stable descriptive filenames rather than `main.tex`. PDFs are committed under `output/pdf/`; intermediates stay in `.build/`. The [PDF manifest](output/pdf/manifest.json) records source hashes, PDF hashes, and page counts.

## Repository layout

```text
papers/                     four current manuscripts with stable Paper I--IV identities
audits/                     mathematical audit and provenance records
scripts/                    build checks and exact verification
output/pdf/                 committed PDF snapshots and manifest
tests/                      repository regression tests
```

## License

Repository-authored code and documentation are available under the [MIT License](LICENSE). Individual manuscript copyright remains with the author. OpenAI manuscripts are cited as external sources and are not vendored here.
