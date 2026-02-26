# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["Filing"]


class Filing(BaseModel):
    accounting_standard: str
    """Accounting standard used: 'Japan GAAP', 'IFRS', or 'US GAAP'."""

    created_at: datetime
    """When this record was created in Axiora."""

    doc_id: str
    """EDINET document ID (e.g.

    'S100ABCD'). Globally unique identifier for each filing.
    """

    doc_type: str
    """EDINET document type code.

    '120'=annual, '130'=semi-annual, '140'=quarterly, '150'=extraordinary.
    """

    edinet_code: str
    """EDINET submitter code of the filing company."""

    fiscal_year: int
    """Fiscal year the filing covers."""

    period_end: date
    """Last day of the reporting period."""

    period_start: date
    """First day of the reporting period."""

    received_at: datetime
    """When Axiora ingested this filing from EDINET."""

    doc_description: Optional[str] = None
    """Description from EDINET (e.g. '有価証券報告書 第 120 期')."""

    doc_type_label: Optional[str] = None
    """Japanese label for doc_type (e.g. '有価証券報告書')."""

    filed_at: Optional[datetime] = None
    """When the filing was submitted to EDINET. Null if not available."""
