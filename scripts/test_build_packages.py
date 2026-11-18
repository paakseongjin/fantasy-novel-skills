"""Regression checks for packaging. Run with python scripts/test_build_packages.py."""
import io
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from build_packages import PLATFORMS, ROOT, collect, metadata, reuse_archive, same_archive


def zip_with_member(name, data, level):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as package:
        info = zipfile.ZipInfo(name)
        package.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=level)
    return stream.getvalue()


class PackageTests(unittest.TestCase):
    def test_published_platform_instructions_and_references(self):
        skills, _ = collect()
        manifest = json.loads((ROOT / "dist/manifest.json").read_bytes())
        records = {record["path"]: record for record in manifest["packages"]}
        headings = {"gemini": "## Gemini Apps에서 적용", "claude": "## Claude에서 적용",
                    "chatgpt": "## ChatGPT Skills에서 적용"}
        for name, source in skills.items():
            for platform in PLATFORMS:
                with self.subTest(name=name, platform=platform):
                    relative = f"dist/{platform}/{name}.zip"
                    data = (ROOT / relative).read_bytes()
                    self.assertEqual(hashlib.sha256(data).hexdigest(), records[relative]["sha256"])
                    self.assertEqual(len(data), records[relative]["bytes"])
                    prefix = "" if platform == "gemini" else name + "/"
                    with zipfile.ZipFile(io.BytesIO(data)) as package:
                        self.assertCountEqual(package.namelist(), [prefix + path for path in source])
                        body = package.read(prefix + "SKILL.md").decode()
                        self.assertTrue(body.startswith(source["SKILL.md"].decode().rstrip() + "\n\n"))
                        for service, heading in headings.items():
                            self.assertEqual(body.splitlines().count(heading), int(service == platform))
                        for path, content in source.items():
                            if path != "SKILL.md":
                                self.assertEqual(package.read(prefix + path), content)

    def test_colon_in_description(self):
        description = "대사 수정: 호칭과 말투를 보존한다."
        header = "---\nname: dialogue\ndescription: {}\n---\n"
        with self.assertRaises(ValueError):
            metadata(header.format(description))
        for quote in ["'", '"']:
            with self.subTest(quote=quote):
                self.assertEqual(metadata(header.format(quote + description + quote))["description"], description)
        self.assertEqual(metadata(header.format("대상:대사"))["description"], "대상:대사")

    def test_keep_published_bytes_and_replace_outdated_bundle(self):
        text = b"scene and dialogue\n" * 400
        published = zip_with_member("SKILL.md", text, 1)
        rebuilt = zip_with_member("SKILL.md", text, 9)
        self.assertNotEqual(published, rebuilt)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skill.zip"
            path.write_bytes(published)
            self.assertEqual(reuse_archive(path, rebuilt), published)
            edited = zip_with_member("SKILL.md", text + b"new", 9)
            self.assertEqual(reuse_archive(path, edited), edited)
        self.assertFalse(same_archive(zip_with_member("skill.zip", published, 9),
                                      zip_with_member("skill.zip", rebuilt, 9)))


if __name__ == "__main__":
    unittest.main()
