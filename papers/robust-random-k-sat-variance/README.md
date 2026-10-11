# A Robust Linear Upper Bound for the Variance of Random $k$-SAT Hitting Times

For each fixed $k\ge 3$, the paper proves

$$
\operatorname{Var}(H_n)=O(n)
$$

for independent, nonidentically distributed proper-clause streams satisfying a fixed two-sided pointwise comparison with the uniform law. It also proves a more local criterion that replaces the global upper comparison by direct assumptions on conditional root-test densities and root-incidence probabilities.

The proof extends the OpenAI clause-omission and root-test framework and the critical killing potential from the linear-variance theorem for random 3-SAT. It allows arbitrary deterministic time dependence. It proves only an upper bound; a matching lower bound and subgaussian tails do not follow formally from the present deletion-delay estimates.

## Build

```bash
latexmk -pdf main.tex
```

The OpenAI sources are pinned in `references.bib`.
