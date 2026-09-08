"""Authenticate with the browser session `albus login` stored on disk.

When neither `api_key` nor `ALBUS_API_KEY` supplies a credential, a
request is sent as the signed-in user, acting in the organization that
session selected. The file is the one the albus CLI writes: one entry
per API base URL under the config directory.
"""

import json
import os
from pathlib import Path
from typing import Optional, Tuple, Union

import httpx

from .types import BeforeRequestContext, BeforeRequestHook

CONFIG_DIR_ENV = "ALBUS_CONFIG_DIR"
XDG_CONFIG_HOME_ENV = "XDG_CONFIG_HOME"
FILE_NAME = "credentials.json"
VERSION = 1
ORGANIZATION_HEADER = "X-Albus-Organization"


class StoredSessionHook(BeforeRequestHook):
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        if "Authorization" in request.headers:
            return request

        stored = stored_session(hook_ctx.base_url)
        if stored is None:
            return request

        access_token, organization = stored
        request.headers["Authorization"] = f"Bearer {access_token}"
        if organization is not None:
            request.headers[ORGANIZATION_HEADER] = organization

        return request


def credentials_path() -> Path:
    configured = os.environ.get(CONFIG_DIR_ENV)
    if configured:
        return Path(configured) / FILE_NAME

    xdg = os.environ.get(XDG_CONFIG_HOME_ENV)
    if xdg:
        return Path(xdg) / "albus" / FILE_NAME

    return Path.home() / ".config" / "albus" / FILE_NAME


def stored_session(base_url: str) -> Optional[Tuple[str, Optional[str]]]:
    """The stored access token and selected organization for base_url.

    Anything that is not a readable credentials file with an entry for
    this API counts as no session: the request then goes out without a
    credential and the server's 401 says to sign in.
    """
    try:
        document = json.loads(credentials_path().read_text())
    except (OSError, UnicodeDecodeError, ValueError):
        return None

    if not isinstance(document, dict) or document.get("version") != VERSION:
        return None

    entries = document.get("credentials")
    if not isinstance(entries, dict):
        return None

    entry = entries.get(base_url.rstrip("/"))
    if not isinstance(entry, dict):
        return None

    access_token = entry.get("access_token")
    if not isinstance(access_token, str) or not access_token:
        return None

    organization = entry.get("organization_id")
    if not isinstance(organization, str):
        organization = None

    return access_token, organization
