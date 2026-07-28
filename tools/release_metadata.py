"""Validate release versions and built distribution artifacts."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import re
import sys

from packaging.utils import (
    canonicalize_name,
    parse_sdist_filename,
    parse_wheel_filename,
)
from packaging.version import InvalidVersion, Version

PACKAGE_NAME = "albus-sdk"


def normalized_version(value: str) -> Version:
    """Return a normalized PEP 440 version or raise ValueError."""
    try:
        version = Version(value)
    except InvalidVersion as error:
        raise ValueError(f"invalid PEP 440 version: {value}") from error

    if str(version) != value:
        raise ValueError(f"version must be normalized as {version}, received {value}")

    return version


def _match_version(path: Path, pattern: str, label: str) -> str:
    match = re.search(pattern, path.read_text(), re.MULTILINE)
    if match is None:
        raise ValueError(f"could not read {label} from {path}")

    return match.group(1)


def repository_versions(root: Path) -> dict[str, str]:
    """Read each generated source of the SDK version."""
    gen_yaml = root / ".speakeasy/gen.yaml"
    pyproject = root / "pyproject.toml"
    version_module = root / "src/albus_sdk/_version.py"

    python_config = re.search(
        r"^python:\n(?P<body>(?:^[ \t].*(?:\n|$))*)",
        gen_yaml.read_text(),
        re.MULTILINE,
    )
    if python_config is None:
        raise ValueError(f"could not find the Python config in {gen_yaml}")

    config_match = re.search(
        r"^  version: ([^\s]+)$",
        python_config.group("body"),
        re.MULTILINE,
    )
    if config_match is None:
        raise ValueError(f"could not read the SDK version from {gen_yaml}")

    project_section = re.search(
        r"^\[project\]\n(?P<body>.*?)(?=^\[|\Z)",
        pyproject.read_text(),
        re.MULTILINE | re.DOTALL,
    )
    if project_section is None:
        raise ValueError(f"could not find [project] in {pyproject}")

    project_match = re.search(
        r'^version = "([^"]+)"$',
        project_section.group("body"),
        re.MULTILINE,
    )
    if project_match is None:
        raise ValueError(f"could not read the project version from {pyproject}")

    return {
        ".speakeasy/gen.yaml": config_match.group(1),
        "pyproject.toml": project_match.group(1),
        "src/albus_sdk/_version.py": _match_version(
            version_module,
            r'^__version__: str = "([^"]+)"$',
            "generated SDK version",
        ),
    }


def validate_repository_versions(root: Path, expected: str) -> Version:
    """Require every version source to match the requested release."""
    version = normalized_version(expected)
    mismatches = {
        path: value
        for path, value in repository_versions(root).items()
        if value != expected
    }
    if mismatches:
        details = ", ".join(f"{path} has {value}" for path, value in mismatches.items())
        raise ValueError(f"expected version {expected}; {details}")

    return version


def _artifact_details(path: Path) -> tuple[str, Version]:
    if path.name.endswith(".whl"):
        name, version, _build, _tags = parse_wheel_filename(path.name)

        return name, version

    if path.name.endswith(".tar.gz"):
        return parse_sdist_filename(path.name)

    raise ValueError(f"unexpected file in dist/: {path.name}")


def validate_artifacts(
    root: Path,
    expected: str,
) -> list[tuple[Path, str]]:
    """Require one matching wheel and sdist, and return their SHA-256 hashes."""
    version = validate_repository_versions(root, expected)
    dist = root / "dist"
    files = sorted(path for path in dist.iterdir() if path.is_file())
    artifacts = [path for path in files if path.name.endswith((".whl", ".tar.gz"))]
    unexpected = [
        path for path in files if path not in artifacts and path.name != ".gitignore"
    ]
    wheel_count = sum(path.name.endswith(".whl") for path in artifacts)
    sdist_count = sum(path.name.endswith(".tar.gz") for path in artifacts)

    if unexpected:
        names = ", ".join(path.name for path in unexpected)
        raise ValueError(f"unexpected files in dist/: {names}")

    if len(artifacts) != 2 or wheel_count != 1 or sdist_count != 1:
        raise ValueError(
            "dist/ must contain exactly one wheel and one source distribution"
        )

    for artifact in artifacts:
        name, artifact_version = _artifact_details(artifact)
        if canonicalize_name(name) != canonicalize_name(PACKAGE_NAME):
            raise ValueError(
                f"{artifact.name} contains package {name}, expected {PACKAGE_NAME}"
            )
        if artifact_version != version:
            raise ValueError(
                f"{artifact.name} contains version {artifact_version}, "
                f"expected {version}"
            )

    return [
        (artifact, sha256(artifact.read_bytes()).hexdigest()) for artifact in artifacts
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("versions", "artifacts"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("version")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()

    try:
        if args.command == "versions":
            validate_repository_versions(root, args.version)
            print(f"Release metadata matches version {args.version}.")

            return

        artifacts = validate_artifacts(root, args.version)
    except (FileNotFoundError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    print("Release artifacts:")
    for artifact, digest in artifacts:
        print(f"{digest}  {artifact.relative_to(root)}")


if __name__ == "__main__":
    main()
