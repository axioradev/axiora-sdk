# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .meta import Meta
from .peer import Peer
from .ratio import Ratio
from .growth import Growth
from .._models import BaseModel
from .financial import Financial
from .translation import Translation
from .health_score import HealthScore

__all__ = ["CompanyRetrieveResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    created_at: datetime
    """When this company record was first created in Axiora."""

    edinet_code: str
    """EDINET submitter code assigned by FSA (e.g. 'E02144'). Primary identifier."""

    name_jp: str
    """Company name in Japanese (e.g. 'トヨタ自動車株式会社')."""

    updated_at: datetime
    """When this company record was last updated."""

    financials: Optional[List[Financial]] = None
    """Financial data for this company (when expand=financials)."""

    fiscal_year_end: Optional[str] = None
    """Fiscal year-end month as 2-digit string (e.g. '03' for March)."""

    growth: Optional[Growth] = None
    """Growth rates and CAGRs (when expand=growth)."""

    health_score: Optional[HealthScore] = None
    """Financial health score (when expand=health_score)."""

    listing: Optional[str] = None
    """TSE market segment in Japanese (e.g. 'プライム（内国株式）')."""

    listing_en: Optional[str] = None
    """TSE market segment in English (e.g. 'Prime'). Auto-translated from listing."""

    name_en: Optional[str] = None
    """Company name in English. Null if not provided in filings."""

    peers: Optional[List[Peer]] = None
    """Peer companies (when expand=peers)."""

    ratios: Optional[List[Ratio]] = None
    """Computed ratios (when expand=ratios)."""

    sector: Optional[str] = None
    """TSE 33-sector classification in Japanese (e.g. '輸送用機器')."""

    sector_en: Optional[str] = None
    """TSE 33-sector classification in English (e.g.

    'Transportation Equipment'). Auto-translated from sector.
    """

    securities_code: Optional[str] = None
    """TSE securities code, typically 4 digits (e.g.

    '7203'). Null for unlisted companies.
    """

    segments: Optional[List[Dict[str, object]]] = None
    """Business segment data (when expand=segments)."""

    translations: Optional[List[Translation]] = None
    """English translations (when expand=translations)."""


class CompanyRetrieveResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
