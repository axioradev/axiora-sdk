# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CompanyRetrieveFinancialsParams"]


class CompanyRetrieveFinancialsParams(TypedDict, total=False):
    fields: Optional[str]
    """Comma-separated field names"""

    years: int
    """Number of fiscal years"""
