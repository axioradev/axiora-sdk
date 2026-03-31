# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .meta import Meta
from .._models import BaseModel

__all__ = ["ListResponseShareholding", "Data"]


class Data(BaseModel):
    base_date: date
    """Base date of the report"""

    filer_edinet_code: str
    """EDINET code of the filer (investor)"""

    report_type: str
    """Report type: 'initial', 'amendment', or 'correction'"""

    doc_id: Optional[str] = None
    """EDINET document ID for source traceability"""

    filing_reason: Optional[str] = None
    """Reason for filing (amendments only)"""

    has_important_proposal: Optional[bool] = None
    """Whether the holder intends to make an important proposal"""

    holder_name: Optional[str] = None
    """Name of the holder"""

    holder_type: Optional[str] = None
    """'individual' or 'corporation'"""

    holding_purpose_category: Optional[str] = None
    """
    Classified purpose: pure_investment, portfolio_investment, cross_holding,
    management, activist, trading, tender_offer, other
    """

    holding_ratio_pct: Optional[float] = None
    """Holding ratio as percentage"""

    issuer_name: Optional[str] = None
    """Name of the issuer (target company)"""

    issuer_security_code: Optional[str] = None
    """Securities code of the issuer (target company)"""

    previous_holding_ratio_pct: Optional[float] = None
    """Holding ratio from previous report"""

    purpose_of_holding: Optional[str] = None
    """Purpose of holding (original Japanese)"""

    shares_held: Optional[int] = None
    """Total shares held"""

    total_outstanding_shares: Optional[int] = None
    """Total outstanding shares of the issuer"""


class ListResponseShareholding(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
