# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    limit: int
    """Results per page"""

    name: Optional[str]

    offset: int
    """Results to skip (ignored when cursor is set)"""

    sector: Optional[str]

    securities_code: Optional[str]
