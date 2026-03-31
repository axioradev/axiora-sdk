# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CompanyListVotingResultsParams"]


class CompanyListVotingResultsParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    fiscal_year: Optional[int]
    """Filter by fiscal year"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""
