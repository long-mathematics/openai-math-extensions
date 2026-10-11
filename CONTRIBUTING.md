# Working on the manuscripts

1. Create a feature branch from `main`.
2. Edit the appropriate current manuscript in `papers/`.
3. Run `make test`, `make pdf`, `make check`, and `make verify`.
4. Inspect changed PDF pages visually; successful compilation is not a mathematical proof audit.
5. Commit the source, corresponding PDFs, and `output/pdf/manifest.json` together.
6. Open a pull request and review the `Build and check manuscripts` job before merging.

Keep the stable Paper I--III identities and descriptive canonical filenames. Keep mathematical changes separate from editorial, build, and file-organization changes. Audit records under `audits/` should be preserved rather than rewritten to match later conclusions.

README mathematics is part of the website interface. Use `$...$` for inline mathematics and `$$...$$` for display mathematics. Do not use `\\(...\\)`, `\\[...\\]`, manuscript-only macros, or definitions such as `\\newcommand` in README.
