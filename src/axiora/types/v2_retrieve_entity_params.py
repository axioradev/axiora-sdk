# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2RetrieveEntityParams"]


class V2RetrieveEntityParams(TypedDict, total=False):
    include: object
    """Comma-separated fact types; 50 each."""
