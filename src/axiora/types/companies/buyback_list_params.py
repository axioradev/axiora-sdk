# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BuybackListParams"]


class BuybackListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    date_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: reporting period ends on or after this date (YYYY-MM-DD)"""

    date_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Filter: reporting period ends on or before this date (YYYY-MM-DD)"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""
