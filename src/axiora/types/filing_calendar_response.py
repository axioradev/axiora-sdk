# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel

__all__ = ["FilingCalendarResponse", "Data"]


class Data(BaseModel):
    date: str

    filing_count: int


class FilingCalendarResponse(BaseModel):
    data: List[Data]

    meta: Meta
