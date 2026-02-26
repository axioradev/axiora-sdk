# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectorListResponse", "Data"]


class Data(BaseModel):
    company_count: int
    """Number of companies in this sector."""

    sector: str
    """TSE 33-sector name in Japanese."""


class SectorListResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
