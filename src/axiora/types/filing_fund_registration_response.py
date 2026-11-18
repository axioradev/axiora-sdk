# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FilingFundRegistrationResponse", "Data"]


class Data(BaseModel):
    agent: Optional[str] = None

    amends_doc_id: Optional[str] = None
    """EDINET document ID that this amendment refers to."""

    contact_name: Optional[str] = None

    doc_id: str

    doc_type: Literal["030", "040"]

    document_form: Optional[str] = None

    edinet_code: Optional[str] = None
    """EDINET code of the filing issuer or manager."""

    filing_date: Optional[date] = None

    fiscal_period_end: Optional[date] = None

    fiscal_period_start: Optional[date] = None

    fund_code: Optional[str] = None
    """Source G-code, absent when a foreign cover supplies none."""

    fund_name: Optional[str] = None

    hq_address: Optional[str] = None

    industry_code: Optional[str] = None

    issuer_name: Optional[str] = None
    """Filed name of the issuer or asset manager."""

    offering_amount_text: Optional[str] = None
    """Filed offering cap as text."""

    parse_warnings: Optional[List[str]] = None

    place_of_filing: Optional[str] = None

    representative: Optional[str] = None

    telephone: Optional[str] = None


class FilingFundRegistrationResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Dict[str, object]
    """Request metadata."""
