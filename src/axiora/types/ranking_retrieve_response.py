# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["RankingRetrieveResponse", "Data"]


class Data(BaseModel):
    company: Company
    """Company details."""

    fiscal_year: int
    """Fiscal year of the ranked value."""

    metric: str
    """Which metric was used (e.g. 'revenue', 'roe')."""

    rank: int
    """Position in the ranking (1-based)."""

    value: Optional[float] = None
    """The metric value used for ranking."""


class RankingRetrieveResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
