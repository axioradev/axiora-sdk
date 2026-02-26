# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["FilingCalendarResponse", "Data"]


class Data(BaseModel):
    date: str
    """Date in ISO 8601 format (YYYY-MM-DD)."""

    filing_count: int
    """Number of filings received on this date."""


class FilingCalendarResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
