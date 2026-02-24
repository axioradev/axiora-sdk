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
    """Company with optional expanded sub-resources."""

    created_at: datetime

    edinet_code: str

    name_jp: str

    updated_at: datetime

    financials: Optional[List[Financial]] = None

    fiscal_year_end: Optional[str] = None

    growth: Optional[Growth] = None

    health_score: Optional[HealthScore] = None

    listing: Optional[str] = None

    listing_en: Optional[str] = None

    name_en: Optional[str] = None

    peers: Optional[List[Peer]] = None

    ratios: Optional[List[Ratio]] = None

    sector: Optional[str] = None

    sector_en: Optional[str] = None

    securities_code: Optional[str] = None

    segments: Optional[List[Dict[str, object]]] = None

    translations: Optional[List[Translation]] = None


class CompanyRetrieveResponse(BaseModel):
    data: Data
    """Company with optional expanded sub-resources."""

    meta: Meta
