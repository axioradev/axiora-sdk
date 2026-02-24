# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .company import Company
from .._models import BaseModel

__all__ = ["Peer"]


class Peer(BaseModel):
    company: Company

    fiscal_year: int

    net_income: Optional[int] = None

    revenue: Optional[int] = None
