# Exact Observation-Time Stabilization Laws for the Brownian Factor-of-IID Sampler

The sole sampler-specific input is OpenAI's complete joint path-law representation. The paper then proves:

- independent $\mathrm{Gamma}(1/2,8)$ stabilization marks, independent of the sampled configuration;
- exact finite-set and terminal-defect laws;
- Gumbel asymptotics and moment convergence for finite maxima;
- unequal-rate and deterministic-clock extensions;
- a vector I-MMSE entropy-dissipation identity for finite target laws;
- an exact comparison with the full-field Bayes snapshot decision.

The time parameter is Brownian observation time after the reconstructed path field is available. No statement about finitary factors or coding radii is made.

## Build

```bash
latexmk -pdf main.tex
```

The OpenAI source is pinned in `references.bib`.
