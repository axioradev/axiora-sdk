# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GrowthMetrics"]


class GrowthMetrics(BaseModel):
    eps: Optional[float] = None
    """EPS growth rate (%)."""

    gross_profit: Optional[float] = None
    """Gross profit growth rate (%)."""

    net_income: Optional[float] = None
    """Net income growth rate (%)."""

    operating_income: Optional[float] = None
    """Operating income growth rate (%)."""

    revenue: Optional[float] = None
    """Revenue growth rate (%). Positive means growth."""

    total_assets: Optional[float] = None
    """Total assets growth rate (%)."""
