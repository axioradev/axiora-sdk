# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["RankingRetrieveResponse", "Data"]


class Data(BaseModel):
    company: Company

    fiscal_year: int

    metric: str

    rank: int

    value: Optional[float] = None


class RankingRetrieveResponse(BaseModel):
    data: List[Data]

    meta: Meta
