from __future__ import annotations

import asyncio
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from datetime import datetime, timezone

import httpx
import pytest

import albus_sdk
from albus_sdk import Albus, errors, models
from albus_sdk.types import UnrecognizedStr

Handler = Callable[[httpx.Request], httpx.Response]


@contextmanager
def sdk_with_handler(
    handler: Handler,
    *,
    security: models.Security | None = None,
) -> Iterator[Albus]:
    transport = httpx.MockTransport(handler)
    async_client = httpx.AsyncClient(transport=transport)

    with httpx.Client(transport=transport) as client:
        try:
            yield Albus(
                client=client,
                async_client=async_client,
                security=security,
            )
        finally:
            asyncio.run(async_client.aclose())


def test_package_exposes_version() -> None:
    assert albus_sdk.VERSION == albus_sdk.__version__
    assert albus_sdk.VERSION == "0.1.0"


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

    security = models.Security(api_key_auth="organization-key")
    with sdk_with_handler(handler, security=security) as sdk:
        response = sdk.sessions.list_sessions()

    assert response.sessions == []


@pytest.mark.asyncio
async def test_user_token_authentication_and_async_operation() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://albus.sh/api/tokens"
        assert request.headers["authorization"] == "Bearer user-token"

        return httpx.Response(200, json={"tokens": []})

    transport = httpx.MockTransport(handler)
    security = models.Security(bearer_auth="user-token")

    with httpx.Client(transport=transport) as client:
        async with httpx.AsyncClient(transport=transport) as async_client:
            sdk = Albus(
                client=client,
                async_client=async_client,
                security=security,
            )
            response = await sdk.tokens.list_tokens_async()

    assert response.tokens == []


def test_documented_error_is_typed() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={"message": "invalid organization key"},
        )

    security = models.Security(api_key_auth="invalid-key")
    with sdk_with_handler(handler, security=security) as sdk:
        with pytest.raises(errors.ErrUnauthorized) as caught:
            sdk.sessions.list_sessions()

    assert caught.value.data.message == "invalid organization key"
    assert caught.value.status_code == 401


def test_session_state_accepts_future_values() -> None:
    now = datetime.now(timezone.utc)
    session = models.Session(
        id="session-id",
        state="PAUSED",
        created_at=now,
        updated_at=now,
    )

    assert session.state == "PAUSED"
    assert isinstance(session.state, UnrecognizedStr)
