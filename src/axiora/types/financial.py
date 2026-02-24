# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from .._models import BaseModel

__all__ = ["Financial"]


class Financial(BaseModel):
    edinet_code: str

    fiscal_year: int

    period_end: date

    bps: Optional[float] = None

    capital_stock: Optional[int] = None

    cash_and_equivalents: Optional[int] = None

    comprehensive_income: Optional[int] = None

    currency: Optional[str] = None

    data_source: Optional[str] = None

    diluted_eps: Optional[float] = None

    dividends_per_share: Optional[float] = None

    eps: Optional[float] = None

    financing_cf: Optional[int] = None

    income_before_tax: Optional[int] = None

    interim_dividend: Optional[float] = None

    investing_cf: Optional[int] = None

    net_assets: Optional[int] = None

    net_income: Optional[int] = None

    num_employees: Optional[int] = None

    operating_cf: Optional[int] = None

    operating_income: Optional[int] = None

    ordinary_income: Optional[int] = None

    payout_ratio: Optional[float] = None

    pe_ratio: Optional[float] = None

    revenue: Optional[int] = None

    roe: Optional[float] = None

    shares_issued: Optional[int] = None

    source_doc_id: Optional[str] = None

    total_assets: Optional[int] = None

    total_equity: Optional[int] = None

    total_liabilities: Optional[int] = None
