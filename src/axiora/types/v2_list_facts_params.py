# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2ListFactsParams"]


class V2ListFactsParams(TypedDict, total=False):
    as_of: object
    """Point in time: only facts known by then."""

    cursor: object

    entity: object
    """Entity ID, e.g. company:E00883."""

    limit: int

    role: object
    """The entity's role in the fact, e.g. issuer."""

    since: object
    """valid_as_of on or after (YYYY-MM-DD)."""

    type: object
    """Fact type (required). See /v2/types."""

    until: object
    """valid_as_of on or before (YYYY-MM-DD)."""
