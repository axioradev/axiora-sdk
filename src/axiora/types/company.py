# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Company"]


class Company(BaseModel):
    created_at: datetime
    """When this company record was first created in Axiora."""

    edinet_code: str
    """EDINET submitter code assigned by FSA (e.g. 'E02144'). Primary identifier."""

    name_jp: str
    """Company name in Japanese (e.g. 'トヨタ自動車株式会社')."""

    updated_at: datetime
    """When this company record was last updated."""

    fiscal_year_end: Optional[str] = None
    """Fiscal year-end month as 2-digit string (e.g. '03' for March)."""

    listing: Optional[str] = None
    """TSE market segment in Japanese (e.g. 'プライム（内国株式）')."""

    listing_en: Optional[str] = None
    """TSE market segment in English (e.g. 'Prime'). Auto-translated from listing."""

    name_en: Optional[str] = None
    """Company name in English. Null if not provided in filings."""

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
