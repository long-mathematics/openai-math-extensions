# Initial audit and repository repair — October 11, 2026

This record summarizes the first joint audit of the three manuscripts before repository normalization.

## Paper I — heterogeneous four-state Potts capacity

The imported OpenAI posterior moment-saving statement was checked against the pinned source, including closure under arbitrary channel parameters and conditionally independent nonidentical products. The new local moment identities, cubic subadditivity, flow telescoping, and heterogeneous path identity were checked independently. An exact symbolic verifier is retained in `scripts/potts_local_audit.py`.

The manuscript was strengthened by recording the sharp comparison at the quadratic-information level and robust reconstruction under additional terminal noise. A weighted-capacity necessity statement without uniform contraction and its exact one-ray converse were also added.

A proposed full weighted converse on arbitrary trees was not promoted: a stopping-line compression argument loses conditional independence because endpoints below a common branch share internal edge noise.

## Paper II — robust random $k$-SAT variance

The frozen-coordinate formula, one-clause comparison, power-sum drift, root-flip tests, filtration split, tower argument, critical exponent balance, incidence moments, and cap removal were checked. No mathematical defect was found in this pass.

The manuscript now separates the roles of the lower and upper density bounds and records that neither a matching lower variance bound nor sub-Gaussian tails follow automatically from the present argument.

## Paper III — Brownian sampler stabilization

The OpenAI source was checked to ensure that the sampler transfers the complete reconstructed path law, which is the input needed for the continuous-time last-passage functional. The stabilization proof, gamma law, finite-set formulas, Gumbel constants, and clock transforms were checked.

The wording was corrected so that the stabilization variable is consistently a supremum of error times rather than necessarily an attained final error time. The scope now explicitly distinguishes observation-time stabilization from factor coding radius or locality.

## Repository normalization

The canonical repository uses stable Paper I--III identities, descriptive manuscript filenames, committed PDF snapshots under `output/pdf/`, and README links to both PDFs and sources. OpenAI dependencies are pinned to commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
