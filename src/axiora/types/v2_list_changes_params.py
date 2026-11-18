# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2ListChangesParams"]


class V2ListChangesParams(TypedDict, total=False):
    since: Required[str]
    """Facts that became known after this time (ISO 8601)."""

    entity: object

    limit: int

    type: object
    """One fact type; all readable types if omitted."""
