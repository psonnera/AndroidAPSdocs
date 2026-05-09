#!/usr/bin/env bash
set -euo pipefail

lang="${READTHEDOCS_LANGUAGE:-en}"

# EN remains the canonical docs source; translations live in docs/CROWDIN.
if [[ "${lang}" == "en" ]]; then
  source_dir="docs/EN"
else
  # Try a few naming variants because CROWDIN folders mix xx, xx_YY, and aliases.
  candidates=(
    "docs/CROWDIN/${lang}"
    "docs/CROWDIN/${lang//-/_}"
    "docs/CROWDIN/${lang//_/-}"
  )

  if [[ "${lang}" =~ ^([a-z]{2})[-_]([a-z]{2})$ ]]; then
    candidates+=("docs/CROWDIN/${BASH_REMATCH[1]}_${BASH_REMATCH[2]^^}")
  fi

  source_dir=""
  for candidate in "${candidates[@]}"; do
    if [[ -d "${candidate}" ]]; then
      source_dir="${candidate}"
      break
    fi
  done

  if [[ -z "${source_dir}" ]]; then
    echo "ERROR: Could not resolve docs source directory for READTHEDOCS_LANGUAGE=${lang}" >&2
    echo "Checked: ${candidates[*]}" >&2
    exit 1
  fi
fi

echo "RTD language: ${lang}"
echo "Building source: ${source_dir}"

npx vitepress build "${source_dir}" \
  --config docs/EN/.vitepress/config.mjs \
  --outDir "${READTHEDOCS_OUTPUT}/html"
