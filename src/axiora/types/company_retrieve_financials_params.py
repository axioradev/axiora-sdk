# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveFinancialsParams"]


class CompanyRetrieveFinancialsParams(TypedDict, total=False):
    doc_type: str
    """Filing type: 120 (annual), 130 (semi-annual), 140 (quarterly)"""

    fields: Optional[str]
    """Comma-separated field names"""

    split_adjusted: bool
    """
    Adjust per-share values (EPS, BPS, DPS) for detected stock splits so the
    time-series is comparable. Set to false for raw unadjusted values.
    """

    years: int
    """Number of fiscal years"""
