# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompareRetrieveParams"]


class CompareRetrieveParams(TypedDict, total=False):
    codes: Required[str]
    """Comma-separated EDINET or securities codes (max 10)"""

    fiscal_year: Optional[int]
