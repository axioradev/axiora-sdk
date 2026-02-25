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

    capex: Optional[int] = None

    capital_stock: Optional[int] = None

    cash_and_equivalents: Optional[int] = None

    comprehensive_income: Optional[int] = None

    cost_of_sales: Optional[int] = None

    currency: Optional[str] = None

    current_assets: Optional[int] = None

    current_liabilities: Optional[int] = None

    data_source: Optional[str] = None

    deferred_tax_assets: Optional[int] = None

    depreciation: Optional[int] = None

    diluted_eps: Optional[float] = None

    dividends_per_share: Optional[float] = None

    eps: Optional[float] = None

    extraordinary_income: Optional[int] = None

    extraordinary_loss: Optional[int] = None

    financing_cf: Optional[int] = None

    goodwill: Optional[int] = None

    gross_profit: Optional[int] = None

    ibd_current: Optional[int] = None

    ibd_noncurrent: Optional[int] = None

    income_before_tax: Optional[int] = None

    intangible_assets: Optional[int] = None

    interest_expense: Optional[int] = None

    interim_dividend: Optional[float] = None

    inventories: Optional[int] = None

    investing_cf: Optional[int] = None

    investment_securities: Optional[int] = None

    net_assets: Optional[int] = None

    net_income: Optional[int] = None

    non_controlling_interests: Optional[int] = None

    noncurrent_assets: Optional[int] = None

    noncurrent_liabilities: Optional[int] = None

    num_employees: Optional[int] = None

    operating_cf: Optional[int] = None

    operating_income: Optional[int] = None

    ordinary_income: Optional[int] = None

    payout_ratio: Optional[float] = None

    pe_ratio: Optional[float] = None

    ppe: Optional[int] = None

    retained_earnings: Optional[int] = None

    revenue: Optional[int] = None

    rnd_expenses: Optional[int] = None

    roe: Optional[float] = None

    sga: Optional[int] = None

    shares_issued: Optional[int] = None

    source_doc_id: Optional[str] = None

    total_assets: Optional[int] = None

    total_equity: Optional[int] = None

    total_liabilities: Optional[int] = None

    trade_payables: Optional[int] = None

    trade_receivables: Optional[int] = None

    treasury_stock: Optional[int] = None
