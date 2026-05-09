#!/usr/bin/env python3
"""Prune files from docs/CROWDIN that are absent from docs/EN by relative path.

By default this script runs as a dry run and writes a manifest.
Use --apply to delete files.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path


def to_posix_relative(path: Path, base: Path) -> str:
    # Keep matching logic platform-neutral and case-insensitive.
    return path.relative_to(base).as_posix()


def repo_root() -> Path:
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(proc.stdout.strip())


def tracked_paths_under(crowdin_root: Path, repo: Path) -> set[str]:
    rel = crowdin_root.relative_to(repo).as_posix()
    proc = subprocess.run(
        ["git", "ls-files", "--", rel],
        check=True,
        capture_output=True,
        text=True,
    )
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def win_long_path(path: Path) -> str:
    # On Windows, use the extended-length prefix to avoid MAX_PATH issues.
    s = str(path)
    if sys.platform.startswith("win"):
        if s.startswith("\\\\?\\"):
            return s
        if s.startswith("\\\\"):
            return "\\\\?\\UNC\\" + s[2:]
        return "\\\\?\\" + s
    return s


def delete_file_path(path: Path) -> None:
    if not path.exists():
        return
    if sys.platform.startswith("win"):
        Path(win_long_path(path)).unlink(missing_ok=False)
        return
    path.unlink(missing_ok=False)


def gather_orphans(
    en_root: Path,
    crowdin_root: Path,
    markdown_only: bool,
) -> list[dict[str, str]]:
    en_rel = {
        to_posix_relative(p, en_root).lower()
        for p in en_root.rglob("*")
        if p.is_file()
    }

    orphans: list[dict[str, str]] = []

    for lang_dir in sorted(p for p in crowdin_root.iterdir() if p.is_dir()):
        if not (lang_dir / "index.md").exists():
            continue

        lang = lang_dir.name
        for file_path in lang_dir.rglob("*"):
            if not file_path.is_file():
                continue
            if markdown_only and file_path.suffix.lower() != ".md":
                continue

            rel_in_lang = to_posix_relative(file_path, lang_dir)
            if rel_in_lang.lower() in en_rel:
                continue

            orphans.append(
                {
                    "lang": lang,
                    "rel_in_lang": rel_in_lang,
                    "extension": file_path.suffix.lower(),
                    "abs": str(file_path),
                }
            )

    return sorted(orphans, key=lambda x: (x["lang"], x["rel_in_lang"]))


def print_summary(orphans: list[dict[str, str]], markdown_only: bool) -> None:
    scope = "markdown only" if markdown_only else "all file types"
    print(f"Detected {len(orphans)} orphan files ({scope}).")
    if not orphans:
        return

    by_lang = Counter(o["lang"] for o in orphans)
    by_ext = Counter(o["extension"] for o in orphans)

    print("\nTop languages by orphan count:")
    for lang, count in by_lang.most_common(15):
        print(f"  {lang:>8}  {count}")

    print("\nBy extension:")
    for ext, count in by_ext.most_common():
        shown_ext = ext if ext else "<no_ext>"
        print(f"  {shown_ext:>8}  {count}")


def write_manifest(orphans: list[dict[str, str]], out_path: Path, repo: Path) -> None:
    lines = []
    for item in orphans:
        repo_rel = Path(item["abs"]).relative_to(repo).as_posix()
        lines.append(repo_rel)
    out_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def delete_orphans(
    orphans: list[dict[str, str]],
    repo: Path,
    tracked: set[str],
) -> tuple[int, int]:
    removed = 0
    failed = 0

    tracked_paths: list[str] = []
    untracked_paths: list[Path] = []

    for item in orphans:
        abs_path = Path(item["abs"])
        repo_rel = abs_path.relative_to(repo).as_posix()
        if repo_rel in tracked:
            tracked_paths.append(repo_rel)
        else:
            untracked_paths.append(abs_path)

    if tracked_paths:
        chunk_size = 200
        for i in range(0, len(tracked_paths), chunk_size):
            chunk = tracked_paths[i : i + chunk_size]
            try:
                subprocess.run(["git", "rm", "-f", "--ignore-unmatch", "--", *chunk], check=True, capture_output=True)
                removed += len(chunk)
            except Exception as exc:  # noqa: BLE001
                # Fallback to single-file deletes so one problematic path does not block the whole chunk.
                print(f"WARN batch git rm failed for {len(chunk)} tracked files: {exc}")
                for rel in chunk:
                    try:
                        subprocess.run(["git", "rm", "-f", "--ignore-unmatch", "--", rel], check=True, capture_output=True)
                        removed += 1
                    except Exception:
                        # If unlink fails (common on Windows long paths), at least remove from index.
                        try:
                            subprocess.run(["git", "rm", "-f", "--cached", "--ignore-unmatch", "--", rel], check=True, capture_output=True)
                            removed += 1
                        except Exception:  # noqa: BLE001
                            failed += 1

    for abs_path in untracked_paths:
        try:
            delete_file_path(abs_path)
            removed += 1
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"WARN failed to delete {abs_path.relative_to(repo).as_posix()}: {exc}")

    return removed, failed


def prune_empty_dirs(crowdin_root: Path) -> int:
    removed = 0
    dirs = sorted([p for p in crowdin_root.rglob("*") if p.is_dir()], key=lambda p: len(p.parts), reverse=True)
    for d in dirs:
        try:
            next(d.iterdir())
        except StopIteration:
            d.rmdir()
            removed += 1
    return removed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--en-root", default="docs/EN", help="Path to EN source tree")
    parser.add_argument("--crowdin-root", default="docs/CROWDIN", help="Path to CROWDIN tree")
    parser.add_argument("--apply", action="store_true", help="Delete detected orphan files")
    parser.add_argument("--markdown-only", action="store_true", help="Limit to .md files only")
    parser.add_argument("--prune-empty-dirs", action="store_true", help="Remove empty directories after deletion")
    parser.add_argument("--manifest", default=None, help="Manifest output path (default: auto)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo = repo_root()
    en_root = (repo / args.en_root).resolve()
    crowdin_root = (repo / args.crowdin_root).resolve()

    if not en_root.exists():
        print(f"ERROR EN root not found: {en_root}")
        return 2
    if not crowdin_root.exists():
        print(f"ERROR CROWDIN root not found: {crowdin_root}")
        return 2

    orphans = gather_orphans(en_root, crowdin_root, args.markdown_only)
    print_summary(orphans, args.markdown_only)

    manifest_name = "_tmp_crowdin_orphans_md.txt" if args.markdown_only else "_tmp_crowdin_orphans_all.txt"
    manifest_path = (repo / args.manifest).resolve() if args.manifest else (repo / manifest_name)
    write_manifest(orphans, manifest_path, repo)
    print(f"\nManifest written: {manifest_path.relative_to(repo).as_posix()}")

    if not args.apply:
        print("Dry run only. Re-run with --apply to delete.")
        return 0

    tracked = tracked_paths_under(crowdin_root, repo)
    removed, failed = delete_orphans(orphans, repo, tracked)
    print(f"Removed: {removed}")
    print(f"Failed:  {failed}")

    if args.prune_empty_dirs:
        pruned = prune_empty_dirs(crowdin_root)
        print(f"Pruned empty directories: {pruned}")

    print("Done. Review and commit when ready.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
