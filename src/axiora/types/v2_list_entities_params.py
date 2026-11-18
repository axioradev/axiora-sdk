# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2ListEntitiesParams"]


class V2ListEntitiesParams(TypedDict, total=False):
    type: Required[str]
    """Entity type: company, holder or filing."""

    cursor: object

    limit: int

    q: object
    """Name or code contains."""
