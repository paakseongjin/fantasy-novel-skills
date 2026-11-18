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
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = ("chatgpt", "claude", "gemini")
LONGFORM = ("plan-fantasy-longform", "design-character-arcs", "manage-fantasy-foreshadowing",
            "structure-serial-chapters", "design-fantasy-action", "craft-character-dialogue",
            "review-fantasy-manuscript")
WEBNOVEL = ("design-reader-attachment", "lower-opening-barrier", "prevent-serial-drag",
            "audit-dropout-risks")
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
            elif value.startswith("'"):
                if not re.fullmatch(r"'(?:[^']|'')*'", value):
                    raise ValueError(f"Invalid quoted metadata field: {key}")
                value = value[1:-1].replace("''", "'")
            elif re.search(r":(?:\s|$)", value):
                raise ValueError(f"Quote metadata field {key} when its value contains a colon separator")
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
        skills[folder.name] = {str(p.relative_to(folder)).replace("\\", "/"): p.read_text(encoding="utf-8").encode()
                               for p in sorted(folder.rglob("*.md"))}
    core_names = set(skills)
    shared = ROOT / "skills/build-fantasy-world/references"
    modules = json.loads((ROOT / "config/worldbuilding-modules.json").read_text(encoding="utf-8"))
    for item in modules:
        name = item["name"]
        if name in skills:
            raise ValueError(f"Duplicate skill: {name}")
        skills[name] = {"SKILL.md": item["skill_markdown"].encode()}
        for filename in item["references"]:
            if Path(filename).name != filename:
                raise ValueError(f"Invalid reference: {filename}")
            skills[name][f"references/{filename}"] = (shared / filename).read_text(encoding="utf-8").encode()
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
        if name == "route-fantasy-writing" and path == "references/skill-catalog.md":
            # These table cells point into the worldbuilding document, outside the router.
            text = re.sub(
                r"\| `(references/[^\s`]+\.md)` \|$",
                r"| `build-fantasy-world.md`의 `자료: \1` |", text, flags=re.MULTILINE)
        def replace(match):
            label, target = match.groups()
            resolved = local_target(path, target)
            return match.group(0) if resolved is None else f"{label}（이 문서의 자료: {resolved}）"
        parts.append(f"\n---\n\n## 자료: {path}\n\n" + LINK.sub(replace, text))
    return "\n".join(parts).encode()


def skill_bundle(outputs, names, title, date_time=(2026, 11, 15, 0, 0, 0)):
    entries = {}
    for platform in PLATFORMS:
        for name in names:
            entries[f"{platform}/{name}.zip"] = outputs[f"dist/{platform}/{name}.zip"]
    for name in names:
        entries[f"chatgpt-project/{name}.md"] = outputs[f"dist/chatgpt-project/{name}.md"]
    entries["chatgpt-project/project-instructions.md"] = (
        ROOT / "platforms/chatgpt/project-instructions.md").read_text(encoding="utf-8").encode()
    count = len(names)
    entries["사용안내.txt"] = (
        f"{title}\n\n먼저 이 묶음의 압축을 푸세요. 각 서비스 폴더에 개별 ZIP {count}개가 있습니다.\n\n"
        "Gemini Apps에서는 gemini 폴더에서, Claude에서는 claude 폴더에서 "
        "필요한 스킬의 개별 ZIP을 골라 업로드하세요.\n\n"
        "ChatGPT Skills에서는 업로드 화면이 ZIP을 지원할 때 chatgpt 폴더의 개별 ZIP을 선택하세요. "
        "다른 형식을 요구하거나 Skills 메뉴가 보이지 않으면 아래 프로젝트 방식을 이용하세요.\n\n"
        "ChatGPT 프로젝트에서는 chatgpt-project/project-instructions.md의 내용을 프로젝트 지침에 붙여 넣고, "
        "같은 폴더에서 사용할 스킬의 .md 파일을 프로젝트 소스로 추가하세요.\n\n설치 가이드\n"
        "https://github.com/paakseongjin/fantasy-novel-skills/blob/main/docs/installation.md\n"
    ).encode()
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path, content in sorted(entries.items()):
            info = zipfile.ZipInfo(path, date_time=date_time)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, content, compresslevel=9)
    with zipfile.ZipFile(io.BytesIO(buffer.getvalue())) as z:
        assert z.testzip() is None
        assert {p: z.read(p) for p in z.namelist()} == entries
    return buffer.getvalue()


def longform_bundle(outputs):
    return skill_bundle(
        outputs, LONGFORM, "장편 판타지 신규 스킬 7개", date_time=(2026, 11, 14, 0, 0, 0))


def webnovel_bundle(outputs):
    return skill_bundle(outputs, WEBNOVEL, "웹소설 연재 점검 스킬 4개")


def expected_outputs():
    skills, core_names = collect()
    instructions = {
        platform: (ROOT / "platforms" / platform / "native-instructions.md").read_text(encoding="utf-8").strip()
        for platform in PLATFORMS
    }
    if not all(instructions.values()) or len(set(instructions.values())) != len(PLATFORMS):
        raise ValueError("Each platform requires distinct, nonempty native instructions")
    outputs = {}
    records = []
    for name, payload in skills.items():
        for platform in PLATFORMS:
            path = f"dist/{platform}/{name}.zip"
            platform_payload = dict(payload)
            platform_payload["SKILL.md"] = payload["SKILL.md"].rstrip() + b"\n\n" + instructions[platform].encode() + b"\n"
            check_payload(name, platform_payload)
            data = reuse_archive(path, archive(name, platform_payload, platform))
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
    for path, build in (("downloads/fantasy-longform-seven-skills.zip", longform_bundle),
                        ("downloads/fantasy-webnovel-serial-skills.zip", webnovel_bundle)):
        outputs[path] = reuse_archive(path, build(outputs))
    return outputs


def reuse_archive(path, expected):
    dest = ROOT / path
    if dest.is_file():
        existing = dest.read_bytes()
        if same_archive(existing, expected):
            return existing
    return expected


def same_archive(actual, expected):
    """Compare ZIP structure and content independently of the zlib version."""
    if actual == expected:
        return True
    try:
        with zipfile.ZipFile(io.BytesIO(actual)) as left, zipfile.ZipFile(io.BytesIO(expected)) as right:
            if left.namelist() != right.namelist():
                return False
            for got, want in zip(left.infolist(), right.infolist()):
                fields = ("date_time", "create_system", "external_attr", "compress_type")
                if any(getattr(got, field) != getattr(want, field) for field in fields):
                    return False
                got_data, want_data = left.read(got), right.read(want)
                if got_data != want_data:
                    return False
    except (zipfile.BadZipFile, zlib.error, EOFError, RuntimeError):
        return False
    return True


def verify_outputs(outputs):
    stale = []
    manifest_path = "dist/manifest.json"
    manifest = json.loads(outputs[manifest_path])
    for path, expected in outputs.items():
        if path == manifest_path:
            continue
        dest = ROOT / path
        if not dest.is_file():
            stale.append(path)
            continue
        actual = dest.read_bytes()
        if actual != expected:
            stale.append(path)

    manifest_file = ROOT / manifest_path
    try:
        actual_manifest = json.loads(manifest_file.read_bytes())
    except (FileNotFoundError, UnicodeError, json.JSONDecodeError):
        actual_manifest = None
    if actual_manifest != manifest:
        stale.append(manifest_path)

    expected_dist = {path for path in outputs if path.startswith("dist/")}
    actual_dist = {p.relative_to(ROOT).as_posix() for p in (ROOT / "dist").rglob("*") if p.is_file()}
    return stale + sorted(actual_dist - expected_dist)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated files without writing")
    args = parser.parse_args()
    outputs = expected_outputs()
    if not args.check:
        for path, data in outputs.items():
            dest = ROOT / path
            if dest.is_file() and dest.read_bytes() == data:
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
    errors = verify_outputs(outputs)
    if errors:
        print("Stale, missing, or unexpected generated files:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    zip_count = sum(p.startswith("dist/") and p.endswith(".zip") for p in outputs)
    doc_count = sum(p.startswith("dist/chatgpt-project/") for p in outputs)
    print(f"{'Verified' if args.check else 'Built'} {zip_count} ZIPs, {doc_count} project documents, and manifest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
