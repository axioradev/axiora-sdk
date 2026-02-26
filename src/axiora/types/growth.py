# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .growth_metrics import GrowthMetrics

__all__ = ["Growth", "Cagr", "Yoy"]


class Cagr(BaseModel):
    """Compound annual growth rates (3-year and 5-year)."""

    api_3yr: Optional[GrowthMetrics] = FieldInfo(alias="3yr", default=None)
    """3-year compound annual growth rates."""

    api_5yr: Optional[GrowthMetrics] = FieldInfo(alias="5yr", default=None)
    """5-year compound annual growth rates."""


class Yoy(BaseModel):
    fiscal_year: int
    """Fiscal year."""

    growth: GrowthMetrics
    """Year-over-year growth rates for this fiscal year."""

    period_end: Optional[str] = None
    """Last day of the fiscal period (ISO 8601)."""


class Growth(BaseModel):
    cagr: Cagr
    """Compound annual growth rates (3-year and 5-year)."""

    yoy: List[Yoy]
    """Year-over-year growth rates for each fiscal year."""
