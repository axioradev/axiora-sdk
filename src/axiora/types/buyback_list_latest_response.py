# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .meta import Meta
from .._models import BaseModel

__all__ = ["BuybackListLatestResponse", "Data"]


class Data(BaseModel):
    edinet_code: str
    """EDINET code of the company"""

    reporting_period_end: date
    """End date of the reporting period"""

    reporting_period_start: date
    """Start date of the reporting period"""

    resolution_type: str
    """Resolution type: 'shareholder_meeting' or 'board_of_directors'"""

    amount_acquired_month: Optional[int] = None
    """Total amount spent on share acquisitions this month in JPY"""

    authorized_amount: Optional[int] = None
    """Maximum amount authorized for buyback in JPY"""

    authorized_shares: Optional[int] = None
    """Maximum shares authorized for buyback under this resolution"""

    cumulative_amount: Optional[int] = None
    """Total amount spent since the buyback resolution date in JPY"""

    cumulative_shares: Optional[int] = None
    """Total shares acquired since the buyback resolution date"""

    progress_amount_pct: Optional[float] = None
    """Buyback completion rate by amount: cumulative / authorized \\** 100"""

    progress_shares_pct: Optional[float] = None
    """Buyback completion rate by shares: cumulative / authorized \\** 100"""

    share_class: Optional[str] = None
    """Class of shares (e.g. '普通株式' for common stock)"""

    shares_acquired_month: Optional[int] = None
    """Number of shares acquired during this reporting month"""

    shares_issued: Optional[int] = None
    """Total shares issued (including treasury shares)"""

    treasury_shares_held: Optional[int] = None
    """Treasury shares held by the company at end of the reporting period"""


class BuybackListLatestResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
