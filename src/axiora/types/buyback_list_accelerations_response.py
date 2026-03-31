# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["BuybackListAccelerationsResponse", "Data"]


class Data(BaseModel):
    edinet_code: str
    """EDINET code"""

    acceleration_pct: Optional[float] = None
    """Increase in completion % (pp)"""

    authorized_shares: Optional[int] = None
    """Authorized shares"""

    current_completion_pct: Optional[float] = None
    """Current period completion %"""

    name: Optional[str] = None
    """Company name"""

    period_end: Optional[str] = None
    """Reporting period end (ISO date)"""

    prev_completion_pct: Optional[float] = None
    """Previous period completion %"""

    resolution_type: Optional[str] = None
    """Resolution type"""

    sector: Optional[str] = None
    """Sector"""


class BuybackListAccelerationsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
