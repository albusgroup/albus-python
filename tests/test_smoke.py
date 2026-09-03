from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Iterator
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timezone
from inspect import signature

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
    access_token: str | None = None,
) -> AsyncIterator[AsyncAlbus]:
    transport = httpx.MockTransport(handler)
    async_client = httpx.AsyncClient(transport=transport)

    try:
        yield AsyncAlbus(
            async_client=async_client,
            access_token=access_token,
        )
    finally:
        await async_client.aclose()


def test_package_exposes_version() -> None:
    assert albus_sdk.VERSION == albus_sdk.__version__
    assert albus_sdk.VERSION == "0.12.0"


def test_default_production_url_and_sync_operation() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert str(request.url) == "https://albus.sh/api/health"

        return httpx.Response(200, json={"status": "ok"})

    with sdk_with_handler(handler) as sdk:
        response = sdk.health.health()

    assert response.status == "ok"


def test_organization_key_authentication() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://albus.sh/api/sessions"
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
        assert str(request.url) == "https://albus.sh/api/tokens"
        assert request.headers["authorization"] == "Bearer user-token"

        return httpx.Response(200, json={"tokens": []})

    transport = httpx.MockTransport(handler)
    async with (
        httpx.AsyncClient(transport=transport) as client,
        AsyncAlbus(
            async_client=client,
            access_token="user-token",
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


def test_constructor_rejects_multiple_authentication_methods() -> None:
    with pytest.raises(ValueError, match="api_key and access_token"):
        Albus(api_key="organization-key", access_token="user-token")

    with pytest.raises(TypeError, match="unexpected keyword argument 'security'"):
        Albus(security=models.Security(api_key="organization-key"))


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
