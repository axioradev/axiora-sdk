# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ...meta import Meta
from ...._models import BaseModel

__all__ = ["TrajectoryGetFilerTrajectoryResponse", "Data", "DataPoint"]


class DataPoint(BaseModel):
    base_date: date
    """Date of the shareholding report"""

    delta_pct: float
    """Change from previous point in pp"""

    holding_ratio_pct: float
    """Holding ratio as percentage"""

    report_type: str
    """Report type"""

    doc_id: Optional[str] = None
    """EDINET document ID (e.g. 'S100ABCD')"""

    purpose_category: Optional[str] = None
    """Classified purpose"""

    shares_held: Optional[int] = None
    """Shares held"""


class Data(BaseModel):
    filer_canonical_code: str
    """Canonical EDINET code of the filer"""

    filing_count: int
    """Total number of filings"""

    issuer_security_code: str
    """Securities code of the issuer"""

    streak_length: int
    """Consecutive filings in current direction"""

    trajectory_type: str
    """accumulating, exiting, stable, or new_position"""

    velocity_pp_per_month: float
    """Percentage points change per month"""

    delta_180d_pct: Optional[float] = None
    """Change in holding ratio over 180 days"""

    delta_1y_pct: Optional[float] = None
    """Change in holding ratio over 1 year"""

    delta_90d_pct: Optional[float] = None
    """Change in holding ratio over 90 days"""

    filer_name: Optional[str] = None
    """Name of the filer"""

    first_base_date: Optional[date] = None
    """Date of first filing"""

    issuer_name: Optional[str] = None
    """Name of the issuer"""

    last_base_date: Optional[date] = None
    """Date of most recent filing"""

    latest_holding_ratio_pct: Optional[float] = None
    """Latest holding ratio"""

    points: Optional[List[DataPoint]] = None
    """Full trajectory points (only in detail endpoint)"""

    purpose_category: Optional[str] = None
    """Latest classified purpose"""


class TrajectoryGetFilerTrajectoryResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
