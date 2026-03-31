# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["EarningListSignalsResponse", "Data"]


class Data(BaseModel):
    actual_value: Optional[float] = None

    company_name: Optional[str] = None

    detected_date: Optional[str] = None

    expected_value: Optional[float] = None

    fiscal_year_end: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    metric: Optional[str] = None

    period_type: Optional[str] = None

    securities_code: Optional[str] = None

    signal_type: Optional[str] = None

    surprise_pct: Optional[float] = None


class EarningListSignalsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
