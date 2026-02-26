# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["TimeseryRetrieveResponse", "Data", "DataPoint"]


class DataPoint(BaseModel):
    fiscal_year: int
    """Fiscal year."""

    period_end: Optional[str] = None
    """Last day of the fiscal period (ISO 8601)."""

    value: Optional[float] = None
    """Metric value for this fiscal year. Null if data is unavailable."""


class Data(BaseModel):
    company: Company
    """Company details."""

    metric: str
    """Which metric is charted (e.g. 'revenue', 'roe')."""

    points: List[DataPoint]
    """Time series data points ordered by fiscal year."""


class TimeseryRetrieveResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
