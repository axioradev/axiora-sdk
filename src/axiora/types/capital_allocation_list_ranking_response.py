# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .capital_allocation import CapitalAllocation

__all__ = ["CapitalAllocationListRankingResponse"]


class CapitalAllocationListRankingResponse(BaseModel):
    data: List[CapitalAllocation]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
