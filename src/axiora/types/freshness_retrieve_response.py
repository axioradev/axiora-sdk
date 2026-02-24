# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["FreshnessRetrieveResponse", "Data"]


class Data(BaseModel):
    filings_this_week: int

    filings_today: int

    total_companies: int

    total_filings: int

    lag_minutes: Optional[int] = None

    last_ingest_at: Optional[str] = None

    last_ingest_status: Optional[str] = None

    next_poll_at: Optional[str] = None


class FreshnessRetrieveResponse(BaseModel):
    data: Data

    meta: Meta
