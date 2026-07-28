"""Normalize known Speakeasy output differences for the local MVP workflow."""

from pathlib import Path
import runpy

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

PUBLISHING_PROMPT = """> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


"""


def normalize_lines(path: Path) -> None:
    lines = [line.rstrip() for line in path.read_text().splitlines()]
    while lines and not lines[-1]:
        lines.pop()

    path.write_text("\n".join(lines) + "\n")


def normalize_readme() -> None:
    path = REPOSITORY_ROOT / "README.md"
    content = path.read_text()
    content = content.replace(PUBLISHING_PROMPT, "")
    if "To finish publishing your SDK to PyPI" in content:
        raise RuntimeError("unexpected Speakeasy publishing prompt was generated")

    path.write_text(content)
    normalize_lines(path)


def normalize_package_metadata() -> None:
    path = REPOSITORY_ROOT / "pyproject.toml"
    content = path.read_text()
    old_license = 'license = { text = "MIT" }'
    new_license = 'license = "MIT"'

    if old_license in content:
        content = content.replace(old_license, new_license, 1)
    elif new_license not in content:
        raise RuntimeError("expected MIT license metadata was not generated")

    path.write_text(content)
    normalize_lines(path)


def main() -> None:
    normalize_readme()
    normalize_package_metadata()
    normalize_lines(REPOSITORY_ROOT / "src/albus_sdk/utils/datetimes.py")

    prepare_readme = REPOSITORY_ROOT / "scripts/prepare_readme.py"
    runpy.run_path(str(prepare_readme), run_name="__main__")


if __name__ == "__main__":
    main()
