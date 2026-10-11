from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "01-heterogeneous-potts-capacity": "heterogeneous-potts-capacity.tex",
    "02-robust-random-k-sat-variance": "robust-random-k-sat-variance.tex",
    "03-brownian-sampler-stabilization": "brownian-sampler-stabilization.tex",
}

class RepositoryTest(unittest.TestCase):
    def test_numbered_paper_layout(self):
        dirs = {p.name for p in (ROOT / "papers").iterdir() if p.is_dir()}
        self.assertEqual(dirs, set(EXPECTED))

    def test_distinguished_entrypoint_names(self):
        for directory, filename in EXPECTED.items():
            paper = ROOT / "papers" / directory
            self.assertTrue((paper / filename).exists())
            self.assertFalse((paper / "main.tex").exists())

    def test_no_draft_names(self):
        bad = []
        for p in (ROOT / "papers").rglob("*"):
            if p.is_file() and ("revised" in p.name.lower() or re.search(r"20\d\d[-_]\d\d[-_]\d\d", p.name)):
                bad.append(str(p.relative_to(ROOT)))
        self.assertEqual(bad, [])

    def test_pdf_names(self):
        expected = {filename.replace(".tex", ".pdf") for filename in EXPECTED.values()}
        actual = {p.name for p in (ROOT / "output" / "pdf").glob("*.pdf")}
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
