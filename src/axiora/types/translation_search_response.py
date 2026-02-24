# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["TranslationSearchResponse", "Data"]


class Data(BaseModel):
    doc_id: str

    edinet_code: str

    fiscal_year: int

    rank: float

    section: str

    snippet: str

    company_name: Optional[str] = None


class TranslationSearchResponse(BaseModel):
    data: List[Data]

    meta: Meta
