# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2SearchParams"]


class V2SearchParams(TypedDict, total=False):
    q: Required[str]
    """Company name or code, or holder name."""

    limit: int

    type: object
    """company or holder; both if omitted."""
