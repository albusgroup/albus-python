from __future__ import annotations

from pathlib import Path

import pytest

from tools.release_metadata import (
    normalized_version,
    repository_versions,
    validate_artifacts,
    validate_repository_versions,
)


def write_version_sources(root: Path, version: str) -> None:
    (root / ".speakeasy").mkdir()
    (root / "src/albus_sdk").mkdir(parents=True)
    (root / ".speakeasy/gen.yaml").write_text(
        f"configVersion: 2.0.0\npython:\n  version: {version}\n"
    )
    (root / "pyproject.toml").write_text(
        f'[project]\nname = "albus-sdk"\nversion = "{version}"\n'
    )
    (root / "src/albus_sdk/_version.py").write_text(f'__version__: str = "{version}"\n')


@pytest.mark.parametrize("version", ["0.1.0", "1.0.0rc1", "2.3.4.post1"])
def test_normalized_version_accepts_pep_440(version: str) -> None:
    assert str(normalized_version(version)) == version


@pytest.mark.parametrize("version", ["v0.1.0", "1.0-rc1", "latest"])
def test_normalized_version_rejects_non_normalized_input(version: str) -> None:
    with pytest.raises(ValueError):
        normalized_version(version)


def test_repository_versions_must_all_match(tmp_path: Path) -> None:
    write_version_sources(tmp_path, "0.1.0")

    assert repository_versions(tmp_path) == {
        ".speakeasy/gen.yaml": "0.1.0",
        "pyproject.toml": "0.1.0",
        "src/albus_sdk/_version.py": "0.1.0",
    }
    assert str(validate_repository_versions(tmp_path, "0.1.0")) == "0.1.0"

    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(pyproject.read_text().replace("0.1.0", "0.2.0"))

    with pytest.raises(ValueError, match="pyproject.toml has 0.2.0"):
        validate_repository_versions(tmp_path, "0.1.0")


def test_artifacts_must_be_one_matching_wheel_and_sdist(
    tmp_path: Path,
) -> None:
    write_version_sources(tmp_path, "0.1.0")
    dist = tmp_path / "dist"
    dist.mkdir()
    wheel = dist / "albus_sdk-0.1.0-py3-none-any.whl"
    sdist = dist / "albus_sdk-0.1.0.tar.gz"
    wheel.write_bytes(b"wheel")
    sdist.write_bytes(b"sdist")

    artifacts = validate_artifacts(tmp_path, "0.1.0")

    assert [path for path, _digest in artifacts] == [wheel, sdist]
    assert all(len(digest) == 64 for _path, digest in artifacts)

    (dist / "unexpected.txt").write_text("do not publish")

    with pytest.raises(ValueError, match="unexpected files"):
        validate_artifacts(tmp_path, "0.1.0")
