"""Normalize known Speakeasy output differences for the local MVP workflow."""

from pathlib import Path
import runpy
import shutil

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

PUBLISHING_PROMPT = """> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


"""

INSTALLATION_REPLACEMENTS = {
    "uv add git+https://github.com/albusgroup/albus-python.git": ("uv add albus-sdk"),
    "pip install git+https://github.com/albusgroup/albus-python.git": (
        "pip install albus-sdk"
    ),
    "poetry add git+https://github.com/albusgroup/albus-python.git": (
        "poetry add albus-sdk"
    ),
}

INVALID_RETRY_EXAMPLE = """    res = albus.secrets.list_secrets(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))
"""

VALID_RETRY_EXAMPLE = """    res = albus.secrets.list_secrets(
        retries=RetryConfig(
            "backoff",
            BackoffStrategy(1, 50, 1.1, 100),
            False,
        )
    )
"""

INVALID_RETRY_EXAMPLE_ASYNC = """        res = await albus.secrets.list_secrets(,
            RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))
"""

VALID_RETRY_EXAMPLE_ASYNC = """        res = await albus.secrets.list_secrets(
            retries=RetryConfig(
                "backoff",
                BackoffStrategy(1, 50, 1.1, 100),
                False,
            )
        )
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

    for generated, published in INSTALLATION_REPLACEMENTS.items():
        content = content.replace(generated, published)

    content = content.replace(INVALID_RETRY_EXAMPLE, VALID_RETRY_EXAMPLE)
    content = content.replace(INVALID_RETRY_EXAMPLE_ASYNC, VALID_RETRY_EXAMPLE_ASYNC)

    if "To finish publishing your SDK to PyPI" in content:
        raise RuntimeError("unexpected Speakeasy publishing prompt was generated")
    if "git+https://github.com/albusgroup/albus-python.git" in content:
        raise RuntimeError("unexpected Git installation command was generated")
    if "list_secrets(," in content:
        raise RuntimeError("invalid retry example was generated")

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

    issues_url = 'urls.issues = "https://github.com/albusgroup/albus-python/issues"'
    if issues_url not in content:
        documentation_url = (
            'urls.documentation = "https://github.com/albusgroup/albus-python#readme"'
        )
        if documentation_url not in content:
            raise RuntimeError("expected documentation URL was not generated")

        content = content.replace(
            documentation_url,
            f"{documentation_url}\n{issues_url}",
            1,
        )

    # The handwritten tests import tools/, which is not on the generated
    # pytest path.
    generated_pythonpath = 'pythonpath = ["src"]'
    repository_pythonpath = 'pythonpath = ["src", "."]'
    if repository_pythonpath not in content:
        if generated_pythonpath not in content:
            raise RuntimeError("expected pytest pythonpath was not generated")

        content = content.replace(
            generated_pythonpath,
            repository_pythonpath,
            1,
        )

    path.write_text(content)
    normalize_lines(path)


def normalize_contributing() -> None:
    source = REPOSITORY_ROOT / "tools/templates/CONTRIBUTING.md"
    destination = REPOSITORY_ROOT / "CONTRIBUTING.md"
    shutil.copyfile(source, destination)
    normalize_lines(destination)


def remove_generated_publisher() -> None:
    (REPOSITORY_ROOT / "scripts/publish.sh").unlink(missing_ok=True)


def normalize_pypi_readme() -> None:
    path = REPOSITORY_ROOT / "README-PYPI.md"
    content = path.read_text()
    absolute_anchor = "https://github.com/albusgroup/albus-python/blob/master/#"
    content = content.replace(absolute_anchor, "#")
    path.write_text(content)
    normalize_lines(path)


def main() -> None:
    normalize_readme()
    normalize_package_metadata()
    normalize_contributing()
    remove_generated_publisher()
    normalize_lines(REPOSITORY_ROOT / "src/albus_sdk/utils/datetimes.py")

    prepare_readme = REPOSITORY_ROOT / "scripts/prepare_readme.py"
    runpy.run_path(str(prepare_readme), run_name="__main__")
    normalize_pypi_readme()


if __name__ == "__main__":
    main()
