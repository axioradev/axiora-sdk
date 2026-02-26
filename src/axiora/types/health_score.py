# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["HealthScore"]


class HealthScore(BaseModel):
    components: Dict[str, float]
    """Point breakdown by component (e.g.

    {'stability': 15.0, 'profitability': 18.0, 'cash_flow': 7.5}).
    """

    computed_at: datetime
    """When the score was computed."""

    edinet_code: str
    """EDINET submitter code."""

    fiscal_year: int
    """Fiscal year the score is based on."""

    flags: List[str]
    """Risk flags (e.g.

    ['net_loss', 'negative_operating_cf']). Empty list if no flags.
    """

    industry_adjustment: float
    """Industry adjustment points (-5 to +5). Compares against TSE 33-sector medians."""

    score: int
    """Financial health score from 0 to 100. Higher is healthier."""

    data_source: Optional[str] = None
    """Data provenance."""

    methodology: Optional[str] = None
    """Human-readable summary of the scoring methodology."""
