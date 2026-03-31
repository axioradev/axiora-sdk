# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthorizeShowParams"]


class AuthorizeShowParams(TypedDict, total=False):
    client_id: Required[str]

    code_challenge: Required[str]

    redirect_uri: Required[str]

    code_challenge_method: str

    resource: str

    response_type: str

    scope: str

    state: str
