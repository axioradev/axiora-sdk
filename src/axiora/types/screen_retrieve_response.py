# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .company import Company
from .._models import BaseModel

__all__ = ["ScreenRetrieveResponse", "Data", "DataFinancials", "DataMetrics"]


class DataFinancials(BaseModel):
    """Latest financial data."""

    fiscal_year: int
    """Fiscal year of the financial data."""

    current_assets: Optional[int] = None
    """Current assets in JPY."""

    current_liabilities: Optional[int] = None
    """Current liabilities in JPY."""

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

    total_liabilities: Optional[int] = None
    """Total liabilities in JPY."""


class DataMetrics(BaseModel):
    """Computed financial ratios."""

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
    """Latest financial data."""

    metrics: DataMetrics
    """Computed financial ratios."""


class ScreenRetrieveResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
