# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["TimeseryRetrieveResponse", "Data", "DataPoint"]


class DataPoint(BaseModel):
    fiscal_year: int

    period_end: Optional[str] = None

    value: Optional[float] = None


class Data(BaseModel):
    company: Company

    metric: str

    points: List[DataPoint]


class TimeseryRetrieveResponse(BaseModel):
    data: List[Data]

    meta: Meta
