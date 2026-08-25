#!/usr/bin/env python3
"""Package each platform's folder into a standalone zip for GitHub Releases.

Assumes src/build.py has already been run so claude/, chatgpt/, gemini/ are
current — this script doesn't regenerate anything, it just bundles what's
already there. Produces dist/<platform>.zip, one per platform, each
containing only that platform's own folder contents (no src/, no other
platforms) — a self-contained download for someone who only wants Claude,
or only wants ChatGPT.

dist/ is gitignored — these zips are release assets, not repo content;
GitHub Actions runs this at tag-push time and attaches the output to the
release. Run locally the same way if you ever need to check what a release
would contain:

    python3 src/package.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PLATFORMS = ["claude", "chatgpt", "gemini"]

SKIP_NAMES = {".DS_Store"}


def package(platform):
    src_dir = ROOT / platform
    if not src_dir.is_dir():
        raise SystemExit(f"Missing platform folder: {src_dir}")
    DIST.mkdir(parents=True, exist_ok=True)
    out = DIST / f"{platform}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(src_dir.rglob("*")):
            if not path.is_file() or path.name in SKIP_NAMES:
                continue
            arcname = str(path.relative_to(src_dir))
            zi = zipfile.ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            zf.writestr(zi, path.read_bytes())
    print(f"packaged {out.relative_to(ROOT)}")


def main():
    for platform in PLATFORMS:
        package(platform)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
