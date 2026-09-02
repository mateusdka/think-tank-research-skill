from __future__ import annotations

import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ZIP_PATH = DIST / "think-tank-research-portable.zip"
PACKAGE_GLOBS = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "assets/think-tank-research-robots-meeting.png",
    "references/*.md",
    "adapters/*.md",
    "examples/*.md",
    "templates/*.md",
)
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def package_files() -> list[Path]:
    files: set[Path] = set()
    for pattern in PACKAGE_GLOBS:
        files.update(path for path in ROOT.glob(pattern) if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def add_bytes(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build() -> str:
    subprocess.run([sys.executable, "scripts/validate_package.py"], cwd=ROOT, check=True)
    DIST.mkdir(exist_ok=True)

    payload = [(path.relative_to(ROOT).as_posix(), path.read_bytes()) for path in package_files()]
    manifest = "".join(f"{sha256_bytes(data)}  {name}\n" for name, data in payload).encode("utf-8")

    with zipfile.ZipFile(ZIP_PATH, "w") as archive:
        for name, data in payload:
            add_bytes(archive, name, data)
        add_bytes(archive, "MANIFEST.sha256", manifest)

    (DIST / "MANIFEST.txt").write_bytes(manifest)
    zip_digest = sha256_bytes(ZIP_PATH.read_bytes())
    (DIST / "checksums.txt").write_text(f"{zip_digest}  {ZIP_PATH.name}\n", encoding="utf-8")
    return zip_digest


def main() -> int:
    digest = build()
    print(f"PACKAGE: {ZIP_PATH.relative_to(ROOT)}")
    print(f"SHA256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
