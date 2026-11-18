# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IdentifierListParams"]


class IdentifierListParams(TypedDict, total=False):
    id: Required[str]
    """
    Any identifier form. Accepted forms: an EDINET code (E12345), a securities code (7203), a 13-digit corporate number (法人番号), or an investor identifier as returned by /v1/investors/search.
    """
