# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CapitalAllocationListRankingParams"]


class CapitalAllocationListRankingParams(TypedDict, total=False):
    classification: Optional[str]
    """Filter: Returner, Hoarder, Reinvestor, Mixed"""

    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    sector: Optional[str]
    """Filter by sector"""
