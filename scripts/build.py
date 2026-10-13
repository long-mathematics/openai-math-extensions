#!/usr/bin/env python3
"""Compile manuscripts and validate committed PDF snapshots."""

from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"
MANIFEST = OUTPUT / "manifest.json"
BUILD = ROOT / ".build"

DOCUMENTS = [
    ("papers/01-heterogeneous-potts-capacity/heterogeneous-potts-capacity.tex", "heterogeneous-potts-capacity.pdf"),
    ("papers/02-robust-random-k-sat-variance/robust-random-k-sat-variance.tex", "robust-random-k-sat-variance.pdf"),
    ("papers/03-brownian-sampler-stabilization/brownian-sampler-stabilization.tex", "brownian-sampler-stabilization.pdf"),
    ("papers/04-conjugate-fibres-rigidity/conjugate-fibres-rigidity.tex", "conjugate-fibres-rigidity.pdf"),
]

README_ALLOWED_COMMANDS = {
    "Omega", "chi", "ge", "lambda", "operatorname",
}

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_digest(source: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(source.parent.rglob("*")):
        if path.is_file() and path.suffix in {".tex", ".bib"}:
            h.update(str(path.relative_to(source.parent)).encode())
            h.update(b"\0")
            h.update(path.read_bytes())
            h.update(b"\0")
    return h.hexdigest()

def check_sources() -> None:
    for rel, _ in DOCUMENTS:
        source = ROOT / rel
        if not source.exists():
            raise RuntimeError("Missing canonical manuscript source: " + rel)
        if source.name == "main.tex":
            raise RuntimeError("Canonical source may not be named main.tex: " + rel)
        text = source.read_text(encoding="utf-8")
        if "Christopher D. Long" not in text:
            raise RuntimeError("Missing Christopher D. Long attribution: " + rel)

def check_readme_math() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (r"\(", r"\)", r"\[", r"\]", r"\newcommand", r"\renewcommand", r"\def"):
        if token in text:
            raise RuntimeError("README contains forbidden TeX syntax: " + token)
    commands = set(re.findall(r"\\([A-Za-z]+)", text))
    unsupported = sorted(commands - README_ALLOWED_COMMANDS)
    if unsupported:
        raise RuntimeError("README contains unsupported/unreviewed TeX command(s): " + ", ".join(unsupported))
    if text.count("$$") % 2:
        raise RuntimeError("README has unmatched display-math delimiter")

def check_readme_links() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith("#") or re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        local = target.split("#", 1)[0]
        if local and not (ROOT / local).exists():
            raise RuntimeError("Broken README link: " + local)

def check_log(log: str, source: Path) -> None:
    patterns = (
        r"^!",
        r"LaTeX Warning:.*undefined",
        r"Citation .* undefined",
        r"Reference .* undefined",
        r"multiply defined",
        r"Overfull ",
    )
    bad = [line for line in log.splitlines() if any(re.search(p, line) for p in patterns)]
    if bad:
        raise RuntimeError("LaTeX diagnostics in %s:\n%s" % (source, "\n".join(bad[:40])))

def pdf_text(path: Path) -> str:
    return subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True, encoding="utf-8")

def build_one(source: Path, output_name: str, env: dict[str, str]):
    work = BUILD / output_name.removesuffix(".pdf")
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    cmd = [
        "latexmk", "-pdf", "-g", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", "-latexoption=-no-shell-escape", "-outdir=" + str(work),
        source.name,
    ]
    result = subprocess.run(cmd, cwd=source.parent, env=env, capture_output=True, text=True, timeout=300)
    (work / "build-console.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise RuntimeError("LaTeX failed for %s; see %s" % (source, work / "build-console.txt"))
    built = work / (source.stem + ".pdf")
    log = (work / (source.stem + ".log")).read_text(errors="replace")
    check_log(log, source)
    info = subprocess.check_output(["pdfinfo", str(built)], text=True)
    pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    rendered = pdf_text(built)
    if "??" in rendered or "[?]" in rendered:
        raise RuntimeError("Rendered PDF contains unresolved reference markers: " + str(source))
    return built, pages

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    for command in ("latexmk", "pdflatex", "biber", "pdftotext", "pdfinfo"):
        if shutil.which(command) is None:
            raise RuntimeError("Missing dependency: " + command)

    check_sources()
    check_readme_math()

    old = {}
    if args.check:
        if not MANIFEST.exists():
            raise RuntimeError("Missing PDF manifest; run make pdf")
        records = json.loads(MANIFEST.read_text(encoding="utf-8"))["documents"]
        old = {record["source"]: record for record in records}
        if set(old) != {rel for rel, _ in DOCUMENTS}:
            raise RuntimeError("Manifest/source list mismatch; run make pdf")
        for rel, name in DOCUMENTS:
            source = ROOT / rel
            pdf = OUTPUT / name
            record = old[rel]
            if record["source_sha256"] != source_digest(source):
                raise RuntimeError("Source changed; run make pdf: " + rel)
            if not pdf.exists() or record["pdf_sha256"] != digest(pdf):
                raise RuntimeError("Missing or modified PDF; run make pdf: " + name)

    env = dict(os.environ, SOURCE_DATE_EPOCH="1791504000", FORCE_SOURCE_DATE="1", TZ="UTC")
    records = []
    copies = []
    for rel, name in DOCUMENTS:
        source = ROOT / rel
        print("Building " + rel, flush=True)
        built, pages = build_one(source, name, env)
        committed = OUTPUT / name
        if args.check:
            if pdf_text(built) != pdf_text(committed):
                raise RuntimeError("Rebuilt PDF content differs; run make pdf: " + name)
            pdfhash = digest(committed)
        else:
            pdfhash = digest(built)
            copies.append((built, committed))
        records.append({
            "source": rel,
            "source_sha256": source_digest(source),
            "pdf": str(committed.relative_to(ROOT)),
            "pdf_sha256": pdfhash,
            "pages": pages,
        })

    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for built, committed in copies:
            shutil.copyfile(built, committed)
        MANIFEST.write_text(json.dumps({"schema_version": 1, "documents": records}, indent=2) + "\n", encoding="utf-8")

    check_readme_links()
    check_readme_math()
    print("Verified %d manuscripts, PDF snapshots, README links, and README math syntax." % len(DOCUMENTS))

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.SubprocessError, OSError, ValueError, KeyError, AttributeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
