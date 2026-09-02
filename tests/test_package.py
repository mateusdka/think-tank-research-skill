from __future__ import annotations

import hashlib
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

from scripts.validate_package import PRIVATE_PATTERNS, REQUIRED_PATHS


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ZIP_PATH = DIST / "think-tank-research-portable.zip"


class PackageContractTests(unittest.TestCase):
    def test_portable_source_contract(self) -> None:
        missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for hermes_specific_token in (
            "`delegate_task`",
            "`web_search`",
            "`web_extract`",
            "`cronjob`",
            "`write_file`",
        ):
            self.assertNotIn(hermes_specific_token, skill)

        editorial = (ROOT / "references/editorial-review.md").read_text(encoding="utf-8")
        self.assertIn("não invente", editorial.lower())
        self.assertIn("revisão de evidências", editorial.lower())
        self.assertIn("integridade factual", editorial.lower())

        web_adapter = (ROOT / "adapters/web-sandboxes.md").read_text(encoding="utf-8")
        self.assertNotIn("na página de releases", web_adapter.lower())

    def test_private_path_patterns_cover_supported_systems(self) -> None:
        private_paths = (
            "/" + "Users/example/private/report.md",
            "/" + "home/example/private/report.md",
            "C:" + "\\Users\\example\\private\\report.md",
        )
        for private_path in private_paths:
            with self.subTest(private_path=private_path):
                self.assertTrue(any(pattern.search(private_path) for pattern in PRIVATE_PATTERNS))

    def test_validation_and_reproducible_distribution(self) -> None:
        subprocess.run(
            [sys.executable, "scripts/validate_package.py"],
            cwd=ROOT,
            check=True,
        )
        subprocess.run(
            [sys.executable, "scripts/build_distributions.py"],
            cwd=ROOT,
            check=True,
        )
        first_digest = hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest()
        subprocess.run(
            [sys.executable, "scripts/build_distributions.py"],
            cwd=ROOT,
            check=True,
        )
        second_digest = hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest()
        self.assertEqual(first_digest, second_digest)

        with zipfile.ZipFile(ZIP_PATH) as archive:
            names = archive.namelist()
            self.assertIn("SKILL.md", names)
            self.assertIn("MANIFEST.sha256", names)
            self.assertNotIn("AGENTS.md", names)
            self.assertFalse(any(name.startswith("tests/") for name in names))
            self.assertFalse(any(name.startswith("dist/") for name in names))

        checksums = (DIST / "checksums.txt").read_text(encoding="utf-8")
        self.assertIn(first_digest, checksums)
        self.assertIn(ZIP_PATH.name, checksums)


if __name__ == "__main__":
    unittest.main()
