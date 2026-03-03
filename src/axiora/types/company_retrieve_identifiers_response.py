# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .meta import Meta
from .._models import BaseModel

__all__ = ["CompanyRetrieveIdentifiersResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    confidence: float
    """Match confidence (0.0 to 1.0)."""

    edinet_code: str
    """EDINET submitter code (e.g. 'E02144')."""

    match_method: str
    """How identifiers were matched (e.g. 'securities_code', 'edinet_api')."""

    matched_at: datetime
    """When the identifiers were last matched."""

    bloomberg_ticker: Optional[str] = None
    """Bloomberg ticker symbol."""

    isin: Optional[str] = None
    """ISIN (12-character international securities ID)."""

    jpx_code: Optional[str] = None
    """JPX issuer code."""

    lei: Optional[str] = None
    """Legal Entity Identifier (20 characters)."""

    securities_code: Optional[str] = None
    """TSE securities code (e.g. '7203')."""


class CompanyRetrieveIdentifiersResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
