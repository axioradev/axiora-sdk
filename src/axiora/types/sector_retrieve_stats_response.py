# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectorRetrieveStatsResponse", "Data", "DataAggregates"]


class DataAggregates(BaseModel):
    """Aggregate financial statistics."""

    avg_net_income: Optional[float] = None
    """Mean net income in the sector (JPY)."""

    avg_operating_margin: Optional[float] = None
    """Mean operating margin in the sector (%)."""

    avg_revenue: Optional[float] = None
    """Mean revenue in the sector (JPY)."""

    avg_roa: Optional[float] = None
    """Mean ROA in the sector (%)."""

    avg_roe: Optional[float] = None
    """Mean ROE in the sector (%)."""

    max_revenue: Optional[int] = None
    """Maximum revenue in the sector (JPY)."""

    min_revenue: Optional[int] = None
    """Minimum revenue in the sector (JPY)."""

    total_net_income: Optional[int] = None
    """Sum of net income across the sector (JPY)."""

    total_revenue: Optional[int] = None
    """Sum of revenue across all companies in the sector (JPY)."""


class Data(BaseModel):
    """The requested resource object."""

    aggregates: DataAggregates
    """Aggregate financial statistics."""

    company_count: int
    """Number of companies in this sector."""

    sector: str
    """TSE 33-sector name in Japanese."""


class SectorRetrieveStatsResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
