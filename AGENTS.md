# Repository instructions

- Treat `papers/` as the canonical Christopher D. Long manuscript sources.
- Preserve the stable Paper I--III identities and numbered paper directories.
- Canonical manuscript entry points must have descriptive kebab-case filenames. Do not use `main.tex`, dates, draft numbers, or suffixes such as `revised`.
- Generated PDF snapshots belong only in `output/pdf/`; LaTeX intermediates belong only in `.build/`.
- Keep direct PDF and canonical LaTeX links for every current paper in the root README.
- For source changes, run `make test`, `make pdf`, `make check`, and `make verify`. Inspect changed PDF pages visually.
- Commit manuscript sources, matching PDFs, and `output/pdf/manifest.json` together.
- Never silently change theorem hypotheses, author attribution, proof status, dependency status, or the distinction between proved statements and open strengthenings.
- README mathematics must use `$...$` and `$$...$$` only. Do not introduce manuscript-only macros or macro definitions in README math.
- OpenAI source dependencies are pinned to commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; update the pin only deliberately and update `DEPENDENCIES.md` at the same time.
- Use feature branches and pull requests. Do not bypass checks or change repository visibility/licensing without an explicit request.
