# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["Filing"]


class Filing(BaseModel):
    accounting_standard: str

    created_at: datetime

    doc_id: str

    doc_type: str

    edinet_code: str

    fiscal_year: int

    period_end: date

    period_start: date

    received_at: datetime

    doc_description: Optional[str] = None

    doc_type_label: Optional[str] = None

    filed_at: Optional[datetime] = None
