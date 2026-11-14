#!/usr/bin/env python3
"""Check distribution completeness, example IDs, and local Markdown links."""
import re
import sys
from urllib.parse import unquote

from build_packages import ROOT, LINK, collect, expected_outputs


def main():
    errors = []
    skills, core = collect()
    if len(core) != 13 or len(skills) != 21:
        errors.append("Expected 13 core and 8 optional skills")
    counts = {"world": ("W", 24), "names": ("N", 48), "magic": ("M", 24),
              "ranks": ("H", 24), "nations": ("C", 24), "peoples": ("P", 24),
              "religions": ("R", 24), "canon": ("A", 24)}
    for topic, (prefix, count) in counts.items():
        source = ROOT / f"skills/build-fantasy-world/references/{topic}-examples.md"
        ids = re.findall(r"^\| (" + prefix + r"\d{2})\b", source.read_text(), re.M)
        expected = [f"{prefix}{i:02}" for i in range(1, count + 1)]
        if ids != expected:
            errors.append(f"Missing, duplicate, or unordered IDs: {source.name}")
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for _, target in LINK.findall(file.read_text()):
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
    print("PASS: 21 skills, 63 ZIPs, 13 project documents, 216 example IDs, references and links.")
    print("Live platform installation/model execution: not tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
