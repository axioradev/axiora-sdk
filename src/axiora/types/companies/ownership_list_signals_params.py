# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OwnershipListSignalsParams"]


class OwnershipListSignalsParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    include_trivial: bool
    """Include tier 3 (trivial) signals"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    signal_type: Optional[str]
    """Filter by signal type"""
