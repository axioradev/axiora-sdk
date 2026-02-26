# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

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

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return companies updated after this timestamp (ISO 8601).

    Use the sync_token from a previous response.
    """
