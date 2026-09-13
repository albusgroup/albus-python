from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Iterator
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timezone
from inspect import signature
import json
from pathlib import Path
from typing import Optional

import httpx
import pytest

import albus_sdk
from albus_sdk import Albus, AsyncAlbus, errors, models
from albus_sdk.types import UNSET, UnrecognizedStr

Handler = Callable[[httpx.Request], httpx.Response]


@contextmanager
def sdk_with_handler(
    handler: Handler,
    *,
    api_key: str | None = None,
) -> Iterator[Albus]:
    transport = httpx.MockTransport(handler)

    with httpx.Client(transport=transport) as client:
        try:
            yield Albus(
                client=client,
                api_key=api_key,
            )
        finally:
            pass


@asynccontextmanager
async def async_sdk_with_handler(
    handler: Handler,
    *,
    api_key: str | None = None,
) -> AsyncIterator[AsyncAlbus]:
    transport = httpx.MockTransport(handler)
    async_client = httpx.AsyncClient(transport=transport)

    try:
        yield AsyncAlbus(
            async_client=async_client,
            api_key=api_key,
        )
    finally:
        await async_client.aclose()


def test_package_exposes_version() -> None:
    assert albus_sdk.VERSION == albus_sdk.__version__
    assert albus_sdk.VERSION == "0.17.0"


def test_default_production_url_and_sync_operation() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert str(request.url) == "https://albus.sh/api/v1/health"

        return httpx.Response(200, json={"status": "ok"})

    with sdk_with_handler(handler) as sdk:
        response = sdk.health.health()

    assert response.status == "ok"


def test_organization_key_authentication() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://albus.sh/api/v1/sessions?limit=25"
        assert request.headers["authorization"] == "Bearer organization-key"

        return httpx.Response(200, json={"sessions": []})

    transport = httpx.MockTransport(handler)
    with (
        httpx.Client(transport=transport) as client,
        Albus(
            client=client,
            api_key="organization-key",
        ) as sdk,
    ):
        response = sdk.sessions.list_sessions()

    assert response.sessions == []


def test_run_session_defaults_to_a_30_minute_wait() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["wait_timeout_seconds"] == "1800"
        assert request.extensions["timeout"]["read"] == 1860

        return httpx.Response(504, json={"message": "still running"})

    with sdk_with_handler(handler) as sdk:
        with pytest.raises(errors.ErrTimeout):
            sdk.sessions.run_session(
                id="session-id",
                user_prompt="hello",
                agent_name="test-agent",
                agent={"model": {"name": "gpt-4o"}},
            )


@pytest.mark.asyncio
async def test_user_token_authentication_and_async_operation() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://albus.sh/api/v1/tokens"
        assert request.headers["authorization"] == "Bearer user-token"

        return httpx.Response(200, json={"tokens": []})

    transport = httpx.MockTransport(handler)
    async with (
        httpx.AsyncClient(transport=transport) as client,
        AsyncAlbus(
            async_client=client,
            api_key="user-token",
        ) as sdk,
    ):
        response = await sdk.tokens.list_tokens()

    assert response.tokens == []


def test_documented_error_is_typed() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={"message": "invalid organization key"},
        )

    with sdk_with_handler(handler, api_key="invalid-key") as sdk:
        with pytest.raises(errors.ErrUnauthorized) as caught:
            sdk.sessions.list_sessions()

    assert caught.value.data.message == "invalid organization key"
    assert caught.value.status_code == 401


def test_constructor_accepts_only_api_key_for_authentication() -> None:
    for argument in (
        "security",
        "access_token",
        "x_albus_organization",
        "server_idx",
        "url_params",
    ):
        with pytest.raises(
            TypeError, match=f"unexpected keyword argument '{argument}'"
        ):
            Albus(**{argument: "value"})

    for sdk in (Albus, AsyncAlbus):
        parameter = signature(sdk).parameters["api_key"]
        assert parameter.annotation == Optional[str]
        assert parameter.default is None


def test_api_key_environment_fallback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("ALBUS_API_KEY", "environment-key")
    monkeypatch.setenv("ALBUS_CONFIG_DIR", str(tmp_path))
    write_stored_session(tmp_path, "https://albus.sh/api/v1", "session-token", "org-1")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer environment-key"
        assert "x-albus-organization" not in request.headers

        return httpx.Response(200, json={"sessions": []})

    with sdk_with_handler(handler) as sdk:
        sdk.sessions.list_sessions()


def test_stored_session_fallback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv("ALBUS_API_KEY", raising=False)
    monkeypatch.setenv("ALBUS_CONFIG_DIR", str(tmp_path))
    write_stored_session(tmp_path, "https://albus.sh/api/v1", "session-token", "org-1")
    write_stored_session(tmp_path, "http://localhost:8080", "local-token", None)

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer session-token"
        assert request.headers["x-albus-organization"] == "org-1"

        return httpx.Response(200, json={"sessions": []})

    with sdk_with_handler(handler) as sdk:
        sdk.sessions.list_sessions()

    with sdk_with_handler(handler, api_key="") as sdk:
        sdk.sessions.list_sessions()

    def local_handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer local-token"
        assert "x-albus-organization" not in request.headers

        return httpx.Response(200, json={"sessions": []})

    with httpx.Client(transport=httpx.MockTransport(local_handler)) as client:
        Albus(
            client=client, server_url="http://localhost:8080/"
        ).sessions.list_sessions()


def test_no_credential_sends_no_authorization(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv("ALBUS_API_KEY", raising=False)
    monkeypatch.setenv("ALBUS_CONFIG_DIR", str(tmp_path))

    def handler(request: httpx.Request) -> httpx.Response:
        assert "authorization" not in request.headers

        return httpx.Response(401, json={"message": "sign in"})

    with sdk_with_handler(handler) as sdk:
        with pytest.raises(errors.ErrUnauthorized):
            sdk.sessions.list_sessions()


def write_stored_session(
    directory: Path, base_url: str, access_token: str, organization: str | None
) -> None:
    file = directory / "credentials.json"
    document = (
        json.loads(file.read_text())
        if file.exists()
        else {"version": 1, "credentials": {}}
    )
    entry: dict[str, object] = {
        "access_token": access_token,
        "refresh_token": None,
        "expires_at": 4102444800.0,
    }
    if organization is not None:
        entry["organization_id"] = organization

    document["credentials"][base_url] = entry
    file.write_text(json.dumps(document))


def test_session_state_accepts_future_values() -> None:
    now = datetime.now(timezone.utc)
    session = models.Session(
        id="session-id",
        state="PAUSED",
        invocation_count=1,
        created_at=now,
        updated_at=now,
    )

    assert session.state == "PAUSED"
    assert isinstance(session.state, UnrecognizedStr)


def test_only_run_session_accepts_a_per_request_retry_configuration() -> None:
    forbidden_parameters = {"retries", "server_url", "timeout_ms", "http_headers"}

    for sdk in (Albus(), AsyncAlbus()):
        for sdk_name in sdk._sub_sdk_map:
            operations = getattr(sdk, sdk_name)
            for operation_name, operation in type(operations).__dict__.items():
                if operation_name.startswith("_") or not callable(operation):
                    continue

                operation = getattr(operations, operation_name)
                if not callable(operation):
                    continue

                parameters = signature(operation).parameters
                assert not forbidden_parameters.intersection(parameters)
                if operation_name == "run_session":
                    assert parameters["retry_config"].default is UNSET
                    assert parameters["wait_timeout_seconds"].default == 1800
                else:
                    assert "retry_config" not in parameters
