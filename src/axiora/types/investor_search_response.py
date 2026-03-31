# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["InvestorSearchResponse", "Data"]


class Data(BaseModel):
    edinet_code: Optional[str] = None

    name_en: Optional[str] = None

    name_jp: Optional[str] = None

    positions: Optional[int] = None


class InvestorSearchResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
