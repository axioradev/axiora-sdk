# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TranslationSearchParams"]


class TranslationSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    fiscal_year: Optional[int]
    """Filter by fiscal year"""

    limit: int

    offset: int

    section: Optional[str]
    """Filter by section"""
