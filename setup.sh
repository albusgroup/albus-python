#!/usr/bin/env bash

set -Eeuo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$script_dir"
cd "$repo_root"

if [[ "$(uname -s)" != "Darwin" ]]; then
    echo "error: setup.sh currently supports macOS with Homebrew" >&2
    exit 1
fi

if ! command -v brew >/dev/null 2>&1; then
    echo "error: install Homebrew from https://brew.sh first" >&2
    exit 1
fi

brew install uv
uv python install 3.10 3.14

version="$(awk '$1 == "speakeasyVersion:" { print $2; exit }' .speakeasy/workflow.yaml)"
if [[ -z "$version" ]]; then
    echo "error: no Speakeasy version is pinned" >&2
    exit 1
fi

case "$(uname -m)" in
    arm64) architecture=arm64 ;;
    x86_64) architecture=amd64 ;;
    *) echo "error: unsupported macOS architecture: $(uname -m)" >&2; exit 1 ;;
esac

asset="speakeasy_darwin_${architecture}.zip"
release="https://github.com/speakeasy-api/speakeasy/releases/download/v${version}"
temporary_dir="$(mktemp -d)"
trap 'rm -rf "$temporary_dir"' EXIT

curl --fail --location --silent --show-error \
    "$release/checksums.txt" >"$temporary_dir/checksums.txt"
curl --fail --location --silent --show-error \
    "$release/$asset" >"$temporary_dir/$asset"

expected_checksum="$(awk -v asset="$asset" '$2 == asset { print $1 }' \
    "$temporary_dir/checksums.txt")"
actual_checksum="$(shasum -a 256 "$temporary_dir/$asset" | awk '{ print $1 }')"
if [[ -z "$expected_checksum" || "$actual_checksum" != "$expected_checksum" ]]; then
    echo "error: Speakeasy CLI checksum verification failed" >&2
    exit 1
fi

unzip -q "$temporary_dir/$asset" -d "$temporary_dir"
mkdir -p bin
install -m 0755 "$temporary_dir/speakeasy" bin/speakeasy

uv sync --all-groups --frozen
echo "SDK development setup complete. Run: ./tools/check"
