#!/usr/bin/env bash

# Git and version guards shared by tools/publish and tools/mirror-release.
# Source this from a script that has already changed into the client root.
#
# require_release_state <sdk-version> sets release_branch on success.

release_branch=""

require_release_state() {
    local sdk_version="$1"
    local branch remote merge_ref remote_output remote_sha local_sha
    local upstream_branch

    uv run --frozen python tools/release_metadata.py versions "$sdk_version"

    if [[ -n "$(git status --porcelain --untracked-files=normal)" ]]; then
        echo "error: releases require a clean worktree" >&2
        exit 1
    fi

    branch="$(git symbolic-ref --quiet --short HEAD || true)"
    if [[ -z "$branch" ]]; then
        echo "error: releases cannot run from a detached HEAD" >&2
        exit 1
    fi

    remote="$(git config --get "branch.$branch.remote" || true)"
    merge_ref="$(git config --get "branch.$branch.merge" || true)"
    if [[ -z "$remote" || -z "$merge_ref" ]]; then
        echo "error: branch $branch does not have an upstream" >&2
        exit 1
    fi

    if ! remote_output="$(
        git ls-remote --exit-code --refs "$remote" "$merge_ref"
    )"; then
        echo "error: upstream ref $merge_ref does not exist on $remote" >&2
        exit 1
    fi

    remote_sha="$(awk 'NR == 1 { print $1 }' <<<"$remote_output")"
    local_sha="$(git rev-parse HEAD)"
    if [[ "$remote_sha" != "$local_sha" ]]; then
        upstream_branch="${merge_ref#refs/heads/}"
        echo "error: HEAD is not the commit pushed to" \
            "$remote/$upstream_branch" >&2
        exit 1
    fi

    # shellcheck disable=SC2034  # read by the sourcing script
    release_branch="$branch"
}
