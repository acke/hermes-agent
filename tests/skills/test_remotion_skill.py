"""Integrity checks for the vendored Remotion optional skill."""

import re
from pathlib import Path

import pytest

SKILL_DIR = Path(__file__).resolve().parents[2] / "optional-skills" / "creative" / "remotion"
LINK_RE = re.compile(r"\]\(((?:\./|\.\./)?[^)#\s]+\.(?:md|json|ts|tsx|mjs))\)")


def test_frontmatter_description_is_short_sentence():
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    desc = re.search(r"^description: (.*)$", text, re.MULTILINE).group(1)
    assert len(desc) <= 60
    assert desc.endswith(".")


def test_only_one_skill_manifest():
    # Nested SKILL.md files would be discovered as separate skills.
    assert [p.name for p in SKILL_DIR.rglob("SKILL.md")] == ["SKILL.md"]


@pytest.mark.parametrize(
    "md", sorted(SKILL_DIR.rglob("*.md")), ids=lambda p: str(p.relative_to(SKILL_DIR))
)
def test_relative_links_resolve(md):
    for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
        if target.startswith("http"):
            continue
        assert (md.parent / target).exists(), f"{md.name}: broken link {target}"
