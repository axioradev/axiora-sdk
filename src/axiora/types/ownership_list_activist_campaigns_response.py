# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipListActivistCampaignsResponse", "Data"]


class Data(BaseModel):
    filer_code: str
    """Activist filer EDINET code"""

    filing_count: int
    """Total filings"""

    issuer_security_code: str
    """Target company securities code"""

    streak_length: int
    """Consecutive filings in current direction"""

    trajectory_type: str
    """accumulating, stable, exiting, etc."""

    campaign_intensity: Optional[str] = None
    """Campaign intensity: high, medium, low"""

    escalation_signals: Optional[int] = None
    """Number of activist escalation signals"""

    filer_name: Optional[str] = None
    """Activist filer name"""

    first_filing_date: Optional[str] = None
    """First filing date (ISO)"""

    holding_ratio_pct: Optional[float] = None
    """Current holding ratio (%)"""

    important_proposals: Optional[int] = None
    """Number of important proposal filings"""

    issuer_name: Optional[str] = None
    """Target company name"""

    last_filing_date: Optional[str] = None
    """Last filing date (ISO)"""

    velocity_pp_per_month: Optional[float] = None
    """Acquisition pace (pp/month)"""


class OwnershipListActivistCampaignsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
