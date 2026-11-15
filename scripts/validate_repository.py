#!/usr/bin/env python3
"""Check distribution completeness, example IDs, and local Markdown links."""
import re
import sys
from urllib.parse import unquote

from build_packages import ROOT, LINK, collect, expected_outputs


def main():
    errors = []
    skills, core = collect()
    if len(core) != 18 or len(skills) != 26:
        errors.append("Expected 17 creative skills, 1 router, and 8 optional skills")
    router = "route-fantasy-writing"
    catalog = (ROOT / f"skills/{router}/references/skill-catalog.md").read_text(encoding="utf-8")
    targets = re.findall(r"^\| `([a-z0-9-]+)` \|", catalog, re.M)
    if len(targets) != len(set(targets)) or set(targets) != set(skills) - {router}:
        errors.append("Router catalog has missing, unknown, or duplicate skill targets")
    for guide in re.findall(r"`(references/[a-z-]+\.md)`", catalog):
        if guide not in skills["build-fantasy-world"]:
            errors.append(f"Router worldbuilding fallback does not exist: {guide}")
    counts = {"world": ("W", 24), "names": ("N", 48), "magic": ("M", 24),
              "ranks": ("H", 24), "nations": ("C", 24), "peoples": ("P", 24),
              "religions": ("R", 24), "canon": ("A", 24)}
    for topic, (prefix, count) in counts.items():
        source = ROOT / f"skills/build-fantasy-world/references/{topic}-examples.md"
        ids = re.findall(r"^\| (" + prefix + r"\d{2})\b", source.read_text(encoding="utf-8"), re.M)
        expected = [f"{prefix}{i:02}" for i in range(1, count + 1)]
        if ids != expected:
            errors.append(f"Missing, duplicate, or unordered IDs: {source.name}")
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for _, target in LINK.findall(file.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = unquote(target.split("#", 1)[0])
            if not (file.parent / path).exists():
                errors.append(f"Broken link: {file.relative_to(ROOT)} -> {target}")
    outputs = expected_outputs()
    for path, data in outputs.items():
        dest = ROOT / path
        if not dest.is_file() or dest.read_bytes() != data:
            errors.append(f"Generated file differs or missing: {path}")
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "dist").rglob("*") if p.is_file()}
    expected_dist = {p for p in outputs if p.startswith("dist/")}
    if actual != expected_dist:
        errors.append(f"Unexpected dist files: {sorted(actual - expected_dist)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    zip_count = sum(p.startswith("dist/") and p.endswith(".zip") for p in outputs)
    print(f"PASS: {len(skills)} skills, {zip_count} ZIPs, {len(core)} project documents, "
          "216 example IDs, router targets, references and links.")
    print("Live platform installation/model execution: not tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
