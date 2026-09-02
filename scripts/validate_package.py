from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "references/execution-modes.md",
    "references/evidence-review.md",
    "references/editorial-review.md",
    "references/platform-capabilities.md",
    "adapters/hermes.md",
    "adapters/codex.md",
    "adapters/claude-code.md",
    "adapters/web-sandboxes.md",
    "examples/simple-question.md",
    "examples/strategic-report.md",
    "templates/research-brief.md",
    "templates/persona-report.md",
    "templates/final-report.md",
    "scripts/validate_package.py",
    "scripts/build_distributions.py",
)
TEXT_SUFFIXES = {".md", ".py", ".txt"}
HERMES_TOKENS_FORBIDDEN_IN_CORE = (
    "`delegate_task`",
    "`web_search`",
    "`web_extract`",
    "`cronjob`",
    "`write_file`",
)
PRIVATE_PATTERNS = (
    re.compile(r"/" + r"Users/[^/\s]+/"),
    re.compile(r"/" + r"home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
    re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md deve começar com frontmatter YAML")
    try:
        raw = text.split("\n---\n", 1)[0].removeprefix("---\n")
    except IndexError as exc:
        raise ValueError("frontmatter sem fechamento") from exc
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def iter_source_text_files() -> list[Path]:
    ignored_parts = {".git", "dist", "__pycache__"}
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and not ignored_parts.intersection(path.relative_to(ROOT).parts)
    )


def validate() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"arquivo obrigatório ausente: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        try:
            frontmatter = parse_frontmatter(skill)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            if frontmatter.get("name") != "think-tank-research":
                errors.append("frontmatter: name deve ser think-tank-research")
            if not frontmatter.get("description"):
                errors.append("frontmatter: description é obrigatória")
            if not frontmatter.get("version"):
                errors.append("frontmatter: version é obrigatória")
        if len(skill.splitlines()) > 500:
            errors.append("SKILL.md excede 500 linhas")
        for token in HERMES_TOKENS_FORBIDDEN_IN_CORE:
            if token in skill:
                errors.append(f"SKILL.md portátil contém ferramenta específica: {token}")

    for path in iter_source_text_files():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(f"conteúdo potencialmente privado em {relative}: {pattern.pattern}")
        if path.suffix == ".md":
            for target in MARKDOWN_LINK.findall(text):
                clean_target = target.split("#", 1)[0]
                if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                    continue
                if not (path.parent / clean_target).resolve().exists():
                    errors.append(f"link local quebrado em {relative}: {target}")

    editorial_path = ROOT / "references/editorial-review.md"
    if editorial_path.is_file():
        editorial = editorial_path.read_text(encoding="utf-8").lower()
        for phrase in ("não invente", "revisão de evidências", "integridade factual"):
            if phrase not in editorial:
                errors.append(f"revisão editorial não contém proteção: {phrase}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION: PASS")
    print(f"Arquivos de texto verificados: {len(iter_source_text_files())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
