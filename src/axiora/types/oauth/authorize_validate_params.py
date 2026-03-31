# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthorizeValidateParams"]


class AuthorizeValidateParams(TypedDict, total=False):
    api_key: Required[str]

    client_id: Required[str]

    code_challenge: Required[str]

    csrf_token: Required[str]

    redirect_uri: Required[str]

    code_challenge_method: str

    state: str
