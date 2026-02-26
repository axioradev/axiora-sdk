# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["CompareRetrieveResponse", "Data", "DataFinancials", "DataRatios"]


class DataFinancials(BaseModel):
    """Financial data for comparison."""

    bps: Optional[float] = None
    """Book value per share in JPY."""

    current_assets: Optional[int] = None
    """Current assets in JPY."""

    current_liabilities: Optional[int] = None
    """Current liabilities in JPY."""

    eps: Optional[float] = None
    """Earnings per share in JPY."""

    gross_profit: Optional[int] = None
    """Gross profit in JPY."""

    net_income: Optional[int] = None
    """Net income in JPY."""

    operating_income: Optional[int] = None
    """Operating income in JPY."""

    revenue: Optional[int] = None
    """Revenue in JPY."""

    total_assets: Optional[int] = None
    """Total assets in JPY."""

    total_equity: Optional[int] = None
    """Total equity in JPY."""


class DataRatios(BaseModel):
    """Financial ratios for comparison."""

    equity_ratio: Optional[float] = None
    """Equity ratio (%)."""

    net_margin: Optional[float] = None
    """Net margin (%)."""

    operating_margin: Optional[float] = None
    """Operating margin (%)."""

    roa: Optional[float] = None
    """Return on assets (%)."""

    roe: Optional[float] = None
    """Return on equity (%)."""


class Data(BaseModel):
    company: Company
    """Company details."""

    financials: DataFinancials
    """Financial data for comparison."""

    fiscal_year: int
    """Fiscal year of the comparison data."""

    ratios: DataRatios
    """Financial ratios for comparison."""


class CompareRetrieveResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
