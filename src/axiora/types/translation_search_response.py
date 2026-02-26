# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["TranslationSearchResponse", "Data"]


class Data(BaseModel):
    doc_id: str
    """EDINET document ID of the matched filing."""

    edinet_code: str
    """EDINET submitter code of the matched company."""

    fiscal_year: int
    """Fiscal year of the matched filing."""

    rank: float
    """PostgreSQL ts_rank relevance score. Higher means more relevant."""

    section: str
    """Filing section where the match was found."""

    snippet: str
    """Text snippet with matching terms highlighted."""

    company_name: Optional[str] = None
    """Company name in Japanese."""


class TranslationSearchResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
