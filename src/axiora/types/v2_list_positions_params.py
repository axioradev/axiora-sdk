# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2ListPositionsParams"]


class V2ListPositionsParams(TypedDict, total=False):
    as_of: object

    company: object
    """Issuer: EDINET code, securities code or 法人番号."""

    cursor: object

    holder: object
    """Holder: EDINET code, LEI or any Axiora holder id."""

    limit: int

    since: object
