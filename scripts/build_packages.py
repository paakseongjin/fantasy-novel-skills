#!/usr/bin/env python3
"""Build deterministic, instruction-only exports with Python 3.9+ (stdlib only)."""
import argparse
import hashlib
import io
import json
import posixpath
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = ("chatgpt", "claude", "gemini")
LONGFORM = ("plan-fantasy-longform", "design-character-arcs", "manage-fantasy-foreshadowing",
            "structure-serial-chapters", "design-fantasy-action", "craft-character-dialogue",
            "review-fantasy-manuscript")
LINK = re.compile(r"\[([^\]]+)\]\(([^\s)]+)\)")


def metadata(text):
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("Missing YAML frontmatter")
    header = text.split("---\n", 2)[1]
    result = {}
    for line in header.splitlines():
        key, sep, value = line.partition(":")
        if sep:
            value = value.strip()
            if value.startswith('"'):
                value = json.loads(value)
            result[key] = value
    name, description = result.get("name", ""), result.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError(f"Invalid name: {name}")
    if not description or len(description) > 200:
        raise ValueError(f"Invalid description length: {name}: {len(description)}")
    return result


def local_target(file, target):
    if target.startswith(("https://", "http://", "mailto:", "#")):
        return None
    return posixpath.normpath(posixpath.join(posixpath.dirname(file), target.split("#")[0]))


def check_payload(name, payload):
    if metadata(payload["SKILL.md"].decode())["name"] != name:
        raise ValueError(f"Directory/name mismatch: {name}")
    for file, content in payload.items():
        if not file.endswith(".md") or file.startswith("/") or ".." in Path(file).parts:
            raise ValueError(f"Unexpected package file: {file}")
        for _, target in LINK.findall(content.decode()):
            resolved = local_target(file, target)
            if resolved is not None and resolved not in payload:
                raise ValueError(f"Broken skill reference: {name}/{file}: {target}")


def collect():
    skills = {}
    for folder in sorted((ROOT / "skills").iterdir()):
        if not folder.is_dir():
            continue
        skills[folder.name] = {str(p.relative_to(folder)).replace("\\", "/"): p.read_bytes()
                               for p in sorted(folder.rglob("*.md"))}
    core_names = set(skills)
    shared = ROOT / "skills/build-fantasy-world/references"
    modules = json.loads((ROOT / "config/worldbuilding-modules.json").read_text())
    for item in modules:
        name = item["name"]
        if name in skills:
            raise ValueError(f"Duplicate skill: {name}")
        skills[name] = {"SKILL.md": item["skill_markdown"].encode()}
        for filename in item["references"]:
            if Path(filename).name != filename:
                raise ValueError(f"Invalid reference: {filename}")
            skills[name][f"references/{filename}"] = (shared / filename).read_bytes()
    for name, payload in skills.items():
        check_payload(name, payload)
    return dict(sorted(skills.items())), core_names


def archive(name, payload, platform):
    buffer = io.BytesIO()
    prefix = "" if platform == "gemini" else f"{name}/"
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path, content in sorted(payload.items()):
            info = zipfile.ZipInfo(prefix + path, date_time=(2026, 11, 14, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, content, compresslevel=9)
    data = buffer.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        assert z.testzip() is None
        restored = {p[len(prefix):]: z.read(p) for p in z.namelist()}
        assert restored == payload, f"ZIP content mismatch: {name}/{platform}"
    return data


def project_document(name, payload):
    parts = [f"# {name} — 프로젝트용 단일 문서\n\n"
             "생성 파일입니다. 원본은 저장소의 skills 또는 config에 있습니다.\n"
             "이 파일은 네이티브 스킬 설치 파일이 아니라 프로젝트 참고 자료입니다.\n"
             "상대 경로 자료를 찾으라는 지시는 아래의 같은 이름을 가진 '자료' 절을 읽는 것으로 해석하세요.\n"
             "요청과 관련된 절만 참고하고 예시를 확정 설정으로 취급하지 마세요.\n"]
    for path in ["SKILL.md"] + sorted(p for p in payload if p != "SKILL.md"):
        text = payload[path].decode()
        if path == "SKILL.md":
            text = text.split("---\n", 2)[2].lstrip()
        def replace(match):
            label, target = match.groups()
            resolved = local_target(path, target)
            return match.group(0) if resolved is None else f"{label}（이 문서의 자료: {resolved}）"
        parts.append(f"\n---\n\n## 자료: {path}\n\n" + LINK.sub(replace, text))
    return "\n".join(parts).encode()


def longform_bundle(outputs):
    entries = {}
    for platform in PLATFORMS:
        for name in LONGFORM:
            entries[f"{platform}/{name}.zip"] = outputs[f"dist/{platform}/{name}.zip"]
    for name in LONGFORM:
        entries[f"chatgpt-project/{name}.md"] = outputs[f"dist/chatgpt-project/{name}.md"]
    entries["chatgpt-project/project-instructions.md"] = (
        ROOT / "platforms/chatgpt/project-instructions.md").read_bytes()
    entries["사용안내.txt"] = (
        "장편 판타지 신규 스킬 7개\n\n이 묶음을 먼저 압축 해제하세요. chatgpt, claude, "
        "gemini 폴더에는 해당 서비스별 개별 ZIP 7개가 들어 있습니다. 바깥 묶음 전체가 "
        "아니라 필요한 개별 ZIP을 각각 업로드하세요.\n\nChatGPT에서 스킬 업로드를 제공하지 "
        "않는 계정은 프로젝트 지침을 복사하고 chatgpt-project의 필요한 Markdown 문서를 "
        "프로젝트 자료에 추가하세요. 이 방식은 스킬 설치와 다릅니다.\n\n플랫폼의 제공 여부·"
        "계정·메뉴는 다를 수 있으며 실제 계정 설치는 검증하지 않았습니다. 공식 상세 안내: "
        "https://github.com/paakseongjin/fantasy-novel-skills/blob/main/docs/installation.md\n"
    ).encode()
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path, content in sorted(entries.items()):
            info = zipfile.ZipInfo(path, date_time=(2026, 11, 14, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, content, compresslevel=9)
    with zipfile.ZipFile(io.BytesIO(buffer.getvalue())) as z:
        assert z.testzip() is None
        assert {p: z.read(p) for p in z.namelist()} == entries
    return buffer.getvalue()


def expected_outputs():
    skills, core_names = collect()
    outputs = {}
    records = []
    for name, payload in skills.items():
        for platform in PLATFORMS:
            path = f"dist/{platform}/{name}.zip"
            data = archive(name, payload, platform)
            outputs[path] = data
            records.append({"path": path, "sha256": hashlib.sha256(data).hexdigest(),
                            "bytes": len(data), "files": len(payload)})
        if name in core_names:
            outputs[f"dist/chatgpt-project/{name}.md"] = project_document(name, payload)
    report = {"schema": 1, "core_skills": sorted(core_names),
              "optional_worldbuilding_skills": sorted(set(skills) - core_names),
              "zip_count": len(records), "packages": records,
              "live_platform_installation_tested": False}
    outputs["dist/manifest.json"] = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode()
    outputs["downloads/fantasy-longform-seven-skills.zip"] = longform_bundle(outputs)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated files without writing")
    args = parser.parse_args()
    outputs = expected_outputs()
    errors = []
    for path, data in outputs.items():
        dest = ROOT / path
        if args.check:
            if not dest.is_file() or dest.read_bytes() != data:
                errors.append(path)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
    expected = {p for p in outputs if p.startswith("dist/")}
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "dist").rglob("*") if p.is_file()}
    errors.extend(sorted(actual - expected))
    if errors:
        print("Stale, missing, or unexpected generated files:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"{'Verified' if args.check else 'Built'} 63 ZIPs, 13 project documents, and manifest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
