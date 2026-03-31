# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EarningRetrieveLatestParams"]


class EarningRetrieveLatestParams(TypedDict, total=False):
    limit: int

    period_type: Optional[str]
    """Filter: FY, Q1, Q2, Q3"""
