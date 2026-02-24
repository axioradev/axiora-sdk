# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectorListResponse", "Data"]


class Data(BaseModel):
    company_count: int

    sector: str


class SectorListResponse(BaseModel):
    data: List[Data]

    meta: Meta
