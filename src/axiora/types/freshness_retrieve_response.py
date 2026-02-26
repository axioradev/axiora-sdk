# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["FreshnessRetrieveResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    filings_this_week: int
    """Number of filings ingested this week."""

    filings_today: int
    """Number of filings ingested today."""

    total_companies: int
    """Total companies in the database."""

    total_filings: int
    """Total filings in the database."""

    lag_minutes: Optional[int] = None
    """Minutes since last successful ingest. Null if no ingest has run."""

    last_ingest_at: Optional[str] = None
    """Timestamp of the last successful EDINET ingest (ISO 8601)."""

    last_ingest_status: Optional[str] = None
    """Status of the last ingest ('ok' or 'error')."""

    next_poll_at: Optional[str] = None
    """Estimated time of next EDINET poll (ISO 8601)."""


class FreshnessRetrieveResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
