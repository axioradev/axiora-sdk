# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..meta import Meta
from ..._models import BaseModel

__all__ = ["BuybackGetAnalysisResponse", "Data", "DataProgram"]


class DataProgram(BaseModel):
    authorized_amount: Optional[int] = None
    """Authorized amount (JPY)"""

    authorized_shares: Optional[int] = None
    """Authorized shares to buy back"""

    completion_pct: Optional[float] = None
    """Completion percentage (0-100)"""

    cumulative_amount: Optional[int] = None
    """Amount spent so far (JPY)"""

    cumulative_shares: Optional[int] = None
    """Shares bought so far"""

    first_period: Optional[str] = None
    """First reporting period (ISO date)"""

    last_period: Optional[str] = None
    """Last reporting period (ISO date)"""

    months_active: Optional[int] = None
    """Duration in months"""

    pace_pct_per_month: Optional[float] = None
    """Completion % per month"""

    report_count: Optional[int] = None
    """Number of monthly reports filed"""

    resolution_type: Optional[str] = None
    """Resolution type"""


class Data(BaseModel):
    """The requested resource object."""

    edinet_code: str
    """EDINET code"""

    programs: List[DataProgram]
    """Per-program analysis"""

    total_programs: int
    """Number of buyback programs"""


class BuybackGetAnalysisResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
