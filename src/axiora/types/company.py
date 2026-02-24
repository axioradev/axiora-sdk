# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Company"]


class Company(BaseModel):
    created_at: datetime

    edinet_code: str

    name_jp: str

    updated_at: datetime

    fiscal_year_end: Optional[str] = None

    listing: Optional[str] = None

    listing_en: Optional[str] = None

    name_en: Optional[str] = None

    sector: Optional[str] = None

    sector_en: Optional[str] = None

    securities_code: Optional[str] = None
