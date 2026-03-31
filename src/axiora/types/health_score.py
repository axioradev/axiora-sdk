# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["HealthScore"]


class HealthScore(BaseModel):
    components: Dict[str, float]
    """Score breakdown by component (stability, profitability, cash_flow)."""

    computed_at: datetime
    """When the score was computed."""

    edinet_code: str
    """EDINET submitter code."""

    fiscal_year: int
    """Fiscal year the score is based on."""

    flags: List[str]
    """Risk flags (e.g. net_loss, negative_operating_cf)."""

    industry_adjustment: float
    """Industry adjustment points (-5 to +5) vs sector medians."""

    score: int
    """Financial health score from 0 to 100. Higher is healthier."""

    data_source: Optional[str] = None
    """Data provenance."""

    methodology: Optional[str] = None
    """Human-readable summary of the scoring methodology."""
