#!/usr/bin/env python3
"""
migrate-myst-to-vitepress.py

Converts MyST/Sphinx Markdown files in docs/EN to VitePress-compatible Markdown.
- Removes toctree blocks
- Converts admonitions (note, warning, danger, tip, important, admonition)
- Converts tab-set / tab-item to vitepress-plugin-tabs syntax
- Converts include directives to VitePress <!--@include: --> syntax
- Converts MyST anchors (label)= to <a id="label"></a>
- Copies logo and favicon to docs/EN/public/

Usage:
    python utils/migrate-myst-to-vitepress.py [--dry-run]

Does NOT touch the CROWDIN folder.
"""

import os
import re
import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_EN = ROOT / "docs" / "EN"

DRY_RUN = "--dry-run" in sys.argv

# ---------------------------------------------------------------------------
# Mapping: MyST admonition type/class → VitePress container type
# ---------------------------------------------------------------------------
ADMON_TYPE_MAP = {
    "note":       "info",
    "hint":       "tip",
    "tip":        "tip",
    "important":  "warning",
    "warning":    "warning",
    "caution":    "warning",
    "attention":  "warning",
    "danger":     "danger",
    "error":      "danger",
    "seealso":    "info",
}


# ---------------------------------------------------------------------------
# Core converter
# ---------------------------------------------------------------------------

def convert(content: str) -> str:
    """Apply all MyST→VitePress transformations to *content*."""

    # ── 1. Strip toctree blocks ────────────────────────────────────────────
    content = _remove_toctree(content)

    # ── 2. Convert backtick-fenced directives (```{...}) ─────────────────
    content = _convert_backtick_directives(content)

    # ── 3. Convert remaining colon-fenced directives (:::{...}) ──────────
    #      (stand-alone includes / admonitions not inside tab-set)
    content = _convert_colon_directives(content)

    # ── 4. Convert MyST anchors   (label)=  →  <a id="label"></a> ────────
    content = _convert_anchors(content)

    return content


# ---------------------------------------------------------------------------
# Step 1 – Remove toctree blocks
# ---------------------------------------------------------------------------

_TOCTREE_RE = re.compile(
    r'[ \t]*```\{toctree\}.*?```[ \t]*\n?',
    re.DOTALL,
)

def _remove_toctree(content: str) -> str:
    return _TOCTREE_RE.sub('', content)


# ---------------------------------------------------------------------------
# Step 2 – Backtick-fenced directives:  ```{name} title\n...\n```
# ---------------------------------------------------------------------------

# Matches   ```{directive} optional-title
#           :option: value          (zero or more option lines)
#           body
#           ```
# The closing fence must be exactly ``` (3 backticks) on its own line.
_BACKTICK_OPEN_RE = re.compile(r'^(`{3,})\{([\w][\w-]*)\}[ \t]*(.*?)[ \t]*$')


def _convert_backtick_directives(content: str) -> str:
    lines = content.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip('\n')
        m = _BACKTICK_OPEN_RE.match(raw)
        if m:
            fence, directive, title = m.group(1), m.group(2), m.group(3)
            i += 1
            options, body_lines, i = _read_options_and_body_backtick(lines, i, fence)
            converted = _render_backtick_directive(directive, title, options, body_lines)
            out.append(converted)
        else:
            out.append(lines[i])
            i += 1
    return ''.join(out)


def _read_options_and_body_backtick(lines, i, fence):
    """Read option lines then body lines until matching closing fence."""
    options = {}
    body_lines = []
    opt_re = re.compile(r'^:([\w-]+):\s*(.*?)$')
    in_options = True

    while i < len(lines):
        raw = lines[i].rstrip('\n')
        # Closing fence
        if raw.strip() == fence:
            i += 1
            break
        opt_m = opt_re.match(raw)
        if in_options and opt_m and not body_lines:
            options[opt_m.group(1)] = opt_m.group(2).strip()
            i += 1
        else:
            in_options = False
            body_lines.append(lines[i])
            i += 1

    return options, body_lines, i


def _render_backtick_directive(directive, title, options, body_lines):
    body_text = ''.join(body_lines)

    # ── toctree (belt-and-suspenders) ─────────────────────────────────────
    if directive == 'toctree':
        return ''

    # ── tab-set ────────────────────────────────────────────────────────────
    if directive == 'tab-set':
        return _convert_tab_set(body_text)

    # ── admonition with explicit title ────────────────────────────────────
    if directive == 'admonition':
        admon_class = options.get('class', 'info')
        if admon_class == 'dropdown':
            inner = convert(body_text)
            return (
                f'<details>\n'
                f'<summary>{title}</summary>\n\n'
                f'{inner.strip()}\n\n'
                f'</details>\n\n'
            )
        vp_type = ADMON_TYPE_MAP.get(admon_class, 'info')
        return _make_container(vp_type, title, body_text)

    # ── simple admonitions ─────────────────────────────────────────────────
    if directive in ADMON_TYPE_MAP:
        vp_type = ADMON_TYPE_MAP[directive]
        return _make_container(vp_type, title, body_text)

    # ── figure ────────────────────────────────────────────────────────────
    if directive == 'figure':
        alt = options.get('alt', '')
        caption_lines = [l.rstrip() for l in body_lines if l.strip()]
        caption = ' '.join(caption_lines)
        img = f'![{alt}]({title})\n'
        if caption:
            img += f'\n*{caption}*\n'
        return img + '\n'

    # ── unknown: keep body, strip directive wrapper ────────────────────────
    return convert(body_text)


# ---------------------------------------------------------------------------
# Step 3 – Colon-fenced directives:  :::{name} title\n...\n:::
# ---------------------------------------------------------------------------

_COLON_OPEN_RE = re.compile(r'^(:{3,})\{([\w][\w-]*)\}[ \t]*(.*?)[ \t]*$')
_COLON_CLOSE_RE = re.compile(r'^:{3,}[ \t]*$')


def _convert_colon_directives(content: str) -> str:
    lines = content.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip('\n')
        m = _COLON_OPEN_RE.match(raw)
        if m:
            fence, directive, title = m.group(1), m.group(2), m.group(3)
            i += 1
            options, body_lines, i = _read_options_and_body_colon(lines, i, len(fence))
            converted = _render_colon_directive(directive, title, options, body_lines)
            out.append(converted)
        else:
            out.append(lines[i])
            i += 1
    return ''.join(out)


def _read_options_and_body_colon(lines, i, min_fence_len):
    options = {}
    body_lines = []
    opt_re = re.compile(r'^:([\w-]+):\s*(.*?)$')
    in_options = True

    while i < len(lines):
        raw = lines[i].rstrip('\n')
        close_m = re.match(r'^(:{3,})[ \t]*$', raw)
        if close_m and len(close_m.group(1)) >= min_fence_len:
            i += 1
            break
        opt_m = opt_re.match(raw)
        if in_options and opt_m and not body_lines:
            options[opt_m.group(1)] = opt_m.group(2).strip()
            i += 1
        else:
            in_options = False
            body_lines.append(lines[i])
            i += 1

    return options, body_lines, i


def _render_colon_directive(directive, title, options, body_lines):
    body_text = ''.join(body_lines)

    # ── include ────────────────────────────────────────────────────────────
    if directive == 'include':
        target = title.strip()
        return f'<!--@include: ./{target}-->\n'

    # ── tab-item is handled inside tab-set; ignore if seen standalone ─────
    if directive == 'tab-item':
        return convert(body_text)

    # Delegate to backtick handler for all other directives
    return _render_backtick_directive(directive, title, options, body_lines)


# ---------------------------------------------------------------------------
# Tab-set parser
# ---------------------------------------------------------------------------

_TAB_ITEM_RE = re.compile(r'^(:{3,})\{tab-item\}[ \t]*(.*?)[ \t]*$')
_COLON_FENCE_CLOSE_RE = re.compile(r'^:{3,}[ \t]*$')
# Standalone include: :::{include} file.md  (no body / self-closing)
_INLINE_INCLUDE_RE = re.compile(r'^:{3,}\{include\}[ \t]+(\S+)[ \t]*$')


def _convert_tab_set(body_text: str) -> str:
    """Parse tab-items from a tab-set body and emit vitepress-plugin-tabs syntax."""
    lines = body_text.splitlines(keepends=True)
    tabs: list[tuple[str, list]] = []
    current_name: str | None = None
    current_lines: list = []
    depth = 0  # track nested colon fences

    i = 0
    while i < len(lines):
        raw = lines[i].rstrip('\n')

        tab_m = _TAB_ITEM_RE.match(raw)
        if tab_m:
            if current_name is not None:
                tabs.append((current_name, current_lines))
            current_name = tab_m.group(2).strip()
            current_lines = []
            depth = 1
            i += 1
            # Skip option lines immediately after :::{tab-item}
            opt_re = re.compile(r'^:([\w-]+):\s*(.*?)$')
            while i < len(lines) and opt_re.match(lines[i].rstrip('\n')):
                i += 1
            continue

        if current_name is not None:
            # Handle :::{include} as a single-line directive (self-closing):
            # consume it plus its closing ::: without incrementing depth
            inc_m = re.match(r'^(:{3,})\{include\}[ \t]+(\S+)[ \t]*$', raw)
            if inc_m:
                current_lines.append(lines[i])
                i += 1
                # Consume the matching closing ::: (if present)
                while i < len(lines):
                    nxt = lines[i].rstrip('\n')
                    if _COLON_FENCE_CLOSE_RE.match(nxt):
                        i += 1
                        break
                    if nxt.strip() == '':
                        i += 1
                    else:
                        break
                continue

            if _COLON_FENCE_CLOSE_RE.match(raw):
                depth -= 1
                if depth <= 0:
                    i += 1
                    continue
            # Track nested colon opens
            elif _COLON_OPEN_RE.match(raw):
                depth += 1
            current_lines.append(lines[i])
        i += 1

    if current_name is not None:
        tabs.append((current_name, current_lines))

    if not tabs:
        return convert(body_text)

    parts = [':::tabs\n']
    for name, tab_lines in tabs:
        tab_body = ''.join(tab_lines)
        # Convert includes and anchors inside tab body
        tab_body = _convert_inline_includes(tab_body)
        tab_body = _convert_anchors(tab_body)
        parts.append(f'== {name}\n')
        parts.append(tab_body)

    parts.append(':::\n\n')
    return ''.join(parts)


def _convert_inline_includes(text: str) -> str:
    """Convert  :::{include} file  lines to VitePress <!--@include: -->."""
    def repl(m):
        return f'<!--@include: ./{m.group(1).strip()}-->\n'
    return re.sub(
        r'^:{3,}\{include\}[ \t]+(\S+)[ \t]*$',
        repl,
        text,
        flags=re.MULTILINE,
    )


# ---------------------------------------------------------------------------
# Step 4 – MyST anchors
# ---------------------------------------------------------------------------

_ANCHOR_RE = re.compile(r'^[ \t]*\(([^)\n]+)\)=[ \t]*$', re.MULTILINE)


def _convert_anchors(content: str) -> str:
    def repl(m):
        return f'<a id="{m.group(1)}"></a>'
    return _ANCHOR_RE.sub(repl, content)


# ---------------------------------------------------------------------------
# Container helper
# ---------------------------------------------------------------------------

def _make_container(vp_type: str, title: str, body_text: str) -> str:
    inner = convert(body_text.strip())
    header = f'::: {vp_type} {title}' if title else f'::: {vp_type}'
    return f'{header}\n{inner}\n:::\n\n'


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(path: Path) -> bool:
    """Convert one file.  Returns True if changed."""
    try:
        original = path.read_text(encoding='utf-8')
    except Exception as exc:
        print(f'  ERROR reading {path.relative_to(ROOT)}: {exc}')
        return False

    converted = convert(original)
    if converted == original:
        return False

    if not DRY_RUN:
        path.write_text(converted, encoding='utf-8')
    return True


# ---------------------------------------------------------------------------
# Public-dir setup
# ---------------------------------------------------------------------------

def setup_public_dir() -> None:
    public_dir = DOCS_EN / 'public'
    if not DRY_RUN:
        public_dir.mkdir(exist_ok=True)

    for src_name, dst_name in [
        ('androidaps-logo.png', 'androidaps-logo.png'),
        ('favicon.ico',        'favicon.ico'),
    ]:
        src = ROOT / 'docs' / src_name
        dst = public_dir / dst_name
        if src.exists():
            if not DRY_RUN:
                shutil.copy2(src, dst)
            print(f'  {"[dry]" if DRY_RUN else "Copied"} {src_name} -> public/{dst_name}')


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if DRY_RUN:
        print('=== DRY RUN – no files will be written ===\n')

    print(f'Source: {DOCS_EN}\n')

    print('Setting up public/ directory...')
    setup_public_dir()
    print()

    changed = 0
    skipped = 0
    for md_file in sorted(DOCS_EN.rglob('*.md')):
        # Skip build output
        rel = md_file.relative_to(DOCS_EN)
        parts = rel.parts
        if parts and parts[0] in ('_build',):
            continue

        if process_file(md_file):
            print(f'  Converted : {rel}')
            changed += 1
        else:
            skipped += 1

    print(f'\nDone.  Changed: {changed}  Unchanged: {skipped}')
    if DRY_RUN:
        print('\n(no files were written)')
    else:
        print('\nNext steps:')
        print('  npm install')
        print('  npm run docs:dev')


if __name__ == '__main__':
    main()
