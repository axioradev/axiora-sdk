# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2ListFilingsParams"]


class V2ListFilingsParams(TypedDict, total=False):
    cursor: object

    limit: int

    q: object
    """Document ID or description contains."""
