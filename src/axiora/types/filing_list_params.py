# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FilingListParams"]


class FilingListParams(TypedDict, total=False):
    company_code: Optional[str]
    """EDINET or securities code"""

    cursor: Optional[str]
    """Opaque cursor for keyset pagination"""

    date_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Start date (inclusive)"""

    date_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """End date (inclusive)"""

    doc_type: Optional[str]
    """Document type code"""

    limit: int
    """Results per page"""

    offset: int
    """Results to skip (ignored when cursor is set)"""

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return filings received after this timestamp (ISO 8601).

    Use the sync_token from a previous response.
    """
