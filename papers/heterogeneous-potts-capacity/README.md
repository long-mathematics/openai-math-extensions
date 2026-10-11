# A Sharp Capacity Criterion for Heterogeneous Four-State Potts Broadcasting on Trees

For an arbitrary locally finite deterministic rooted tree with edge parameters $0<\lambda_e\le q<1$, the paper proves

$$
\text{reconstruction}
\quad\Longleftrightarrow\quad
\mathrm{Cap}_3(T,\rho)>0,
\qquad
\rho(v)=\prod_{e\in[o,v]}\lambda_e^2.
$$

The theorem removes both the common-channel and uniform-degree assumptions. Further results include:

- two-sided comparison between quadratic root information and capacity;
- equivalence with robust reconstruction under any fixed additional leaf noise;
- an exact spherical-tree series criterion;
- a weighted-capacity necessity theorem for arbitrary $0<\lambda_e\le1$;
- exact weighted capacity on one ray;
- a sharper universal posterior-product estimate with constants verified symbolically.

The necessity direction imports the preserved-class moment-saving theorem from the pinned OpenAI threshold manuscript. The sufficiency and robust-reconstruction directions are independent of that certified input.

## Build and verification

```bash
python verify_local_expansion.py
latexmk -pdf main.tex
```
