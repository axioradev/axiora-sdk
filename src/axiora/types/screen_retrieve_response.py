# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["ScreenRetrieveResponse", "Data", "DataFinancials", "DataMetrics"]


class DataFinancials(BaseModel):
    fiscal_year: int

    net_income: Optional[int] = None

    operating_income: Optional[int] = None

    revenue: Optional[int] = None

    total_assets: Optional[int] = None

    total_equity: Optional[int] = None

    total_liabilities: Optional[int] = None


class DataMetrics(BaseModel):
    equity_ratio: Optional[float] = None

    net_margin: Optional[float] = None

    operating_margin: Optional[float] = None

    roa: Optional[float] = None

    roe: Optional[float] = None


class Data(BaseModel):
    company: Company

    financials: DataFinancials

    metrics: DataMetrics


class ScreenRetrieveResponse(BaseModel):
    data: List[Data]

    meta: Meta
