# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VotingListRecentParams"]


class VotingListRecentParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    limit: int
    """Results per page"""

    min_dissent_pct: Optional[float]
    """Minimum dissent percentage to filter high-opposition proposals (e.g. 20.0)"""

    offset: int
    """Results to skip (ignored when cursor is set)"""
