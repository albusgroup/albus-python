"""Spec-conformance tests: the real HTTP client against a mock of the spec.

Every other test in this package fakes the transport inside the process, so
nothing there exercises a request the SDK actually put on a socket, and nothing
checks that the generated client still agrees with the specification it was
generated from. These do: `tools/conformance` mocks `openapi/openapi.yaml` with
Prism and points the SDK at it, so an operation that sends a request the spec
rejects fails here, and so does one whose response the SDK cannot parse.

The mock answers from the spec, not from the service, so this proves the client
matches the contract — never that the service implements it.
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator

import pytest
import pytest_asyncio

from albus_sdk import Albus, AsyncAlbus, models, operations

MOCK_URL = os.environ.get("ALBUS_CONFORMANCE_URL", "")

pytestmark = pytest.mark.skipif(
    MOCK_URL == "",
    reason="ALBUS_CONFORMANCE_URL is unset; run these through tools/conformance",
)

API_KEY = "conformance-api-key"
ACCESS_TOKEN = "conformance-access-token"


@pytest.fixture
def sdk() -> Iterator[Albus]:
    with Albus(server_url=MOCK_URL, api_key=API_KEY) as sdk:
        yield sdk


@pytest.fixture
def bearer_sdk() -> Iterator[Albus]:
    """For the operations the spec allows `bearer_auth` alone."""
    with Albus(server_url=MOCK_URL, access_token=ACCESS_TOKEN) as sdk:
        yield sdk


@pytest_asyncio.fixture
async def async_sdk() -> AsyncIterator[AsyncAlbus]:
    async with AsyncAlbus(server_url=MOCK_URL, api_key=API_KEY) as sdk:
        yield sdk


def test_health(sdk: Albus) -> None:
    assert isinstance(sdk.health.health(), models.HealthResponse)


def test_whoami(sdk: Albus) -> None:
    assert isinstance(sdk.auth.whoami(), models.WhoamiResponse)


def test_list_models(sdk: Albus) -> None:
    assert isinstance(sdk.models.list_models(), models.ListModelsResponse)


def test_sessions(sdk: Albus) -> None:
    assert isinstance(sdk.sessions.list_sessions(), models.ListSessionsResponse)
    assert isinstance(
        sdk.sessions.get_session(id="conformance-session"),
        models.SessionResponse,
    )
    assert isinstance(
        sdk.sessions.get_session_audit(id="conformance-session", limit=10),
        models.ListAuditEventsResponse,
    )
    sdk.sessions.delete_session(id="conformance-session")


def test_run_session(sdk: Albus) -> None:
    response = sdk.sessions.run_session(
        id="conformance-session",
        user_prompt="What is the conformance of this client?",
        agent_name="conformance",
        agent=models.AgentConfig(
            model=models.Model(name="gemini-3.6-flash"),
            tools=models.Tools(web_search=models.WebSearchTool()),
        ),
        invocation_key="conformance-invocation",
        wait_timeout_seconds=0,
    )

    assert isinstance(response, operations.RunSessionResponse)
    assert isinstance(response.result, models.RunSessionResponse)


def test_secrets(sdk: Albus) -> None:
    assert isinstance(sdk.secrets.list_secrets(), models.ListSecretsResponse)
    assert isinstance(
        sdk.secrets.create_secret(name="conformance", value="secret-value"),
        models.Secret,
    )
    assert isinstance(sdk.secrets.get_secret(name="conformance"), models.Secret)
    sdk.secrets.delete_secret(name="conformance")


def test_tokens(bearer_sdk: Albus) -> None:
    assert isinstance(bearer_sdk.tokens.list_tokens(), models.ListTokensResponse)
    assert isinstance(
        bearer_sdk.tokens.create_token(name="conformance"),
        models.CreateTokenResponse,
    )
    assert isinstance(bearer_sdk.tokens.get_token(id="conformance"), models.Token)
    bearer_sdk.tokens.delete_token(id="conformance")


def test_agents(sdk: Albus) -> None:
    assert isinstance(sdk.agents.list_agents(), models.ListAgentsResponse)
    assert isinstance(sdk.agents.get_agent(name="conformance"), models.Agent)
    assert isinstance(
        sdk.agents.get_agent_revision(name="conformance", revision="1"),
        models.AgentRevision,
    )


@pytest.mark.asyncio
async def test_async_client(async_sdk: AsyncAlbus) -> None:
    assert isinstance(await async_sdk.health.health(), models.HealthResponse)
    assert isinstance(
        await async_sdk.sessions.list_sessions(),
        models.ListSessionsResponse,
    )
