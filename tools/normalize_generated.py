"""Normalize generated output to Albus's supported Python SDK surface."""

from __future__ import annotations

from pathlib import Path
import re
import runpy
import shutil

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
OPERATION_DIRECTORY = REPOSITORY_ROOT / "src/albus_sdk"
SDK_DOCUMENTATION_DIRECTORY = REPOSITORY_ROOT / "docs/sdks"

PUBLISHING_PROMPT = """> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


"""

INSTALLATION_REPLACEMENTS = {
    "uv add git+https://github.com/albusgroup/albus-python.git": "uv add albus-sdk",
    "pip install git+https://github.com/albusgroup/albus-python.git": "pip install albus-sdk",
    "poetry add git+https://github.com/albusgroup/albus-python.git": "poetry add albus-sdk",
}

INVALID_RETRY_EXAMPLE = """    res = albus.secrets.list_secrets(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))
"""

VALID_RETRY_EXAMPLE = """    res = albus.secrets.list_secrets()
"""

INVALID_RETRY_EXAMPLE_ASYNC = """        res = await albus.secrets.list_secrets(,
            RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))
"""

VALID_RETRY_EXAMPLE_ASYNC = """        res = await albus.secrets.list_secrets()
"""

RETRY_PARAMETERS = """        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
"""

RETRY_DOCUMENTATION = """        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
"""

REQUEST_CONFIGURATION = """        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
"""

RETRY_CONFIGURATION = """        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        request_retry_config = None
        if isinstance(retries, utils.RetryConfig):
            request_retry_config = (
                retries,
                [\"429\", \"500\", \"502\", \"503\", \"504\"],
            )

"""

GENERATED_RETRY_CONFIGURATION = """        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [\"429\", \"500\", \"502\", \"503\", \"504\"])

"""


def normalize_lines(path: Path) -> None:
    lines = [line.rstrip() for line in path.read_text().splitlines()]
    while lines and not lines[-1]:
        lines.pop()

    path.write_text("\n".join(lines) + "\n")


def normalize_readme() -> None:
    path = REPOSITORY_ROOT / "README.md"
    content = path.read_text().replace(PUBLISHING_PROMPT, "")

    for generated, published in INSTALLATION_REPLACEMENTS.items():
        content = content.replace(generated, published)
    content = content.replace(INVALID_RETRY_EXAMPLE, VALID_RETRY_EXAMPLE)
    content = content.replace(
        INVALID_RETRY_EXAMPLE_ASYNC,
        VALID_RETRY_EXAMPLE_ASYNC,
    )
    content = re.sub(
        r"(?s)(<!-- Start Retries \[retries\] -->).*?(<!-- End Retries \[retries\] -->)",
        """\\1
## Retries

Only `run_session` supports retries. Configure its default retry policy with
`retry_config` when constructing the SDK, or pass `retry_config` directly to a
single `run_session` invocation. Omit it to inherit the SDK default; pass
`None` to disable retries for that invocation.
\\2""",
        content,
        count=1,
    )

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
    content = content.replace('license = { text = "MIT" }', 'license = "MIT"', 1)

    issues_url = 'urls.issues = "https://github.com/albusgroup/albus-python/issues"'
    documentation_url = (
        'urls.documentation = "https://github.com/albusgroup/albus-python#readme"'
    )
    if issues_url not in content:
        if documentation_url not in content:
            raise RuntimeError("expected documentation URL was not generated")

        content = content.replace(
            documentation_url,
            f"{documentation_url}\n{issues_url}",
            1,
        )

    content = content.replace('pythonpath = ["src"]', 'pythonpath = ["src", "."]')
    path.write_text(content)
    normalize_lines(path)


def normalize_contributing() -> None:
    source = REPOSITORY_ROOT / "tools/templates/CONTRIBUTING.md"
    destination = REPOSITORY_ROOT / "CONTRIBUTING.md"
    if source.exists():
        shutil.copyfile(source, destination)
        normalize_lines(destination)


def normalize_pypi_readme() -> None:
    path = REPOSITORY_ROOT / "README-PYPI.md"
    content = path.read_text().replace(
        "https://github.com/albusgroup/albus-python/blob/master/#", "#"
    )
    path.write_text(content)
    normalize_lines(path)


def normalize_operation_method(content: str) -> str:
    is_run_session = content.startswith("    def run_session(") or content.startswith(
        "    async def run_session("
    )

    if RETRY_PARAMETERS in content:
        replacement = (
            "        retry_config: OptionalNullable[utils.RetryConfig] = UNSET,\n"
            if is_run_session
            else ""
        )
        content = content.replace(RETRY_PARAMETERS, replacement, 1)

    if RETRY_DOCUMENTATION in content:
        replacement = (
            "        :param retry_config: Override the SDK retry configuration for this invocation.\n"
            if is_run_session
            else ""
        )
        content = content.replace(RETRY_DOCUMENTATION, replacement, 1)

    content = content.replace(
        REQUEST_CONFIGURATION,
        "        url_variables = None\n"
        "        base_url = self._get_url(None, url_variables)\n",
        1,
    )
    content = content.replace("            http_headers=http_headers,\n", "", 1)
    content = content.replace(
        "            timeout_ms=timeout_ms,\n",
        "            timeout_ms=self.sdk_configuration.timeout_ms,\n",
        1,
    )

    if GENERATED_RETRY_CONFIGURATION in content:
        replacement = (
            "        retries = retry_config\n\n" + RETRY_CONFIGURATION
            if is_run_session
            else "        retry_config = None\n\n"
        )
        content = content.replace(GENERATED_RETRY_CONFIGURATION, replacement, 1)

    if is_run_session:
        content = content.replace(
            "            retry_config=retry_config,\n",
            "            retry_config=request_retry_config,\n",
            1,
        )
        content = content.replace(
            "        retries = retry_config\n\n" + GENERATED_RETRY_CONFIGURATION,
            "        retries = retry_config\n\n" + RETRY_CONFIGURATION,
            1,
        )
        content = content.replace(
            "        retries = retry_config\n\n"
            "        retries = retry_config\n\n" + RETRY_CONFIGURATION,
            "        retries = retry_config\n\n" + RETRY_CONFIGURATION,
            1,
        )
    else:
        content = content.replace(
            "            retry_config=retry_config,\n",
            "            retry_config=None,\n",
            1,
        )

    return content.replace("        *,\n    ) ->", "    ) ->", 1)


def remove_unused_imports(content: str) -> str:
    if "OptionalNullable" not in content and "UNSET" not in content:
        content = content.replace(
            "from albus_sdk.types import OptionalNullable, UNSET\n", ""
        )
    if "Mapping[" not in content:
        content = content.replace(
            "from typing import Any, Mapping, Optional, Union\n",
            "from typing import Any, Optional, Union\n",
        )
        content = content.replace(
            "from typing import Any, Mapping, Optional\n",
            "from typing import Any, Optional\n",
        )

    return content


def normalize_operation_files() -> None:
    for path in OPERATION_DIRECTORY.glob("*.py"):
        if path.name in {
            "__init__.py",
            "_version.py",
            "basesdk.py",
            "httpclient.py",
            "sdk.py",
            "sdkconfiguration.py",
        }:
            continue

        content = path.read_text()
        methods = re.split(r"(?=^    (?:async )?def )", content, flags=re.MULTILINE)
        if len(methods) == 1:
            continue

        content = methods[0] + "".join(
            normalize_operation_method(method) for method in methods[1:]
        )
        path.write_text(remove_unused_imports(content))
        normalize_lines(path)


def normalize_sdk_documentation() -> None:
    for path in SDK_DOCUMENTATION_DIRECTORY.glob("*/README.md"):
        sections = re.split(r"(?=^## )", path.read_text(), flags=re.MULTILINE)
        normalized_sections = [sections[0]]

        for section in sections[1:]:
            is_run_session = section.startswith("## run_session\n")
            retry_row = next(
                (
                    line
                    for line in section.splitlines(keepends=True)
                    if line.startswith("| `retries`")
                ),
                None,
            )
            if retry_row is None:
                normalized_sections.append(section)
                continue

            if is_run_session:
                replacement = retry_row.replace(
                    "`retries`",
                    "`retry_config`",
                    1,
                ).replace(
                    "Configuration to override the default retry behavior of the client.",
                    "Override the SDK retry configuration for this invocation.",
                    1,
                )
            else:
                replacement = ""

            normalized_sections.append(section.replace(retry_row, replacement, 1))

        path.write_text("".join(normalized_sections))
        normalize_lines(path)


def main() -> None:
    normalize_readme()
    normalize_package_metadata()
    normalize_contributing()
    (REPOSITORY_ROOT / "scripts/publish.sh").unlink(missing_ok=True)
    normalize_lines(REPOSITORY_ROOT / "src/albus_sdk/utils/datetimes.py")
    normalize_operation_files()
    normalize_sdk_documentation()

    prepare_readme = REPOSITORY_ROOT / "scripts/prepare_readme.py"
    runpy.run_path(str(prepare_readme), run_name="__main__")
    normalize_pypi_readme()


if __name__ == "__main__":
    main()
