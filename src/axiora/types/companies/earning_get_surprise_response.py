# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..meta import Meta
from ..._models import BaseModel

__all__ = ["EarningGetSurpriseResponse", "Data", "DataSurprise"]


class DataSurprise(BaseModel):
    actual: Optional[float] = None

    beat: Optional[bool] = None

    forecast: Optional[float] = None

    surprise_pct: Optional[float] = None


class Data(BaseModel):
    accounting_standard: Optional[str] = None

    bps: Optional[float] = None

    cash_end: Optional[int] = None

    company_name: Optional[str] = None

    comprehensive_income: Optional[int] = None

    diluted_eps: Optional[float] = None

    dps_annual: Optional[float] = None

    eps: Optional[float] = None

    equity_ratio_pct: Optional[float] = None

    filing_date: Optional[str] = None

    financing_cf: Optional[int] = None

    fiscal_year_end: Optional[str] = None

    investing_cf: Optional[int] = None

    is_consolidated: Optional[bool] = None

    net_assets: Optional[int] = None

    net_income: Optional[int] = None

    net_income_change_pct: Optional[float] = None

    operating_cf: Optional[int] = None

    operating_income: Optional[int] = None

    operating_income_change_pct: Optional[float] = None

    operating_margin_pct: Optional[float] = None

    ordinary_income: Optional[int] = None

    period_type: Optional[str] = None

    revenue: Optional[int] = None

    revenue_change_pct: Optional[float] = None

    roa_pct: Optional[float] = None

    roe_pct: Optional[float] = None

    securities_code: Optional[str] = None

    surprise: Optional[Dict[str, DataSurprise]] = None

    total_assets: Optional[int] = None


class EarningGetSurpriseResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
