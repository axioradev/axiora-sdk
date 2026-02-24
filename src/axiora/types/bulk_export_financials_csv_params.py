# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BulkExportFinancialsCsvParams"]


class BulkExportFinancialsCsvParams(TypedDict, total=False):
    fields: Optional[str]
    """Comma-separated fields (default: all)"""

    fiscal_year: Optional[int]
    """Filter by fiscal year"""

    sector: Optional[str]
    """Filter by sector"""
