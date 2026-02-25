# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["CompareRetrieveResponse", "Data", "DataFinancials", "DataRatios"]


class DataFinancials(BaseModel):
    bps: Optional[float] = None

    current_assets: Optional[int] = None

    current_liabilities: Optional[int] = None

    eps: Optional[float] = None

    gross_profit: Optional[int] = None

    net_income: Optional[int] = None

    operating_income: Optional[int] = None

    revenue: Optional[int] = None

    total_assets: Optional[int] = None

    total_equity: Optional[int] = None


class DataRatios(BaseModel):
    equity_ratio: Optional[float] = None

    net_margin: Optional[float] = None

    operating_margin: Optional[float] = None

    roa: Optional[float] = None

    roe: Optional[float] = None


class Data(BaseModel):
    company: Company

    financials: DataFinancials

    fiscal_year: int

    ratios: DataRatios


class CompareRetrieveResponse(BaseModel):
    data: List[Data]

    meta: Meta
