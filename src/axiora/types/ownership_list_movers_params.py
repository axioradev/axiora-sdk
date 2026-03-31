# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OwnershipListMoversParams"]


class OwnershipListMoversParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    days: int
    """Look back period in days"""

    limit: int
    """Results per page"""

    min_delta_pct: Optional[float]
    """Minimum absolute delta percentage"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    trajectory_type: Optional[str]
    """Filter: 'accumulating' or 'exiting'"""
