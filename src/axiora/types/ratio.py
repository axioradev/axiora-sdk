# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Ratio"]


class Ratio(BaseModel):
    fiscal_year: int
    """Fiscal year."""

    bps: Optional[float] = None
    """Book value per share in JPY."""

    current_ratio: Optional[float] = None
    """Current ratio.

    Current assets ÷ current liabilities. Above 1.0 means short-term solvency.
    """

    debt_to_equity: Optional[float] = None
    """Debt-to-equity ratio. Total liabilities ÷ total equity."""

    dividends_per_share: Optional[float] = None
    """Annual dividends per share in JPY."""

    eps: Optional[float] = None
    """Basic earnings per share in JPY."""

    equity_ratio: Optional[float] = None
    """Equity ratio (%). Total equity ÷ total assets."""

    gross_margin: Optional[float] = None
    """Gross margin (%). Gross profit ÷ revenue."""

    interest_coverage: Optional[float] = None
    """Interest coverage ratio. Operating income ÷ interest expense."""

    net_margin: Optional[float] = None
    """Net margin (%). Net income ÷ revenue."""

    num_employees: Optional[int] = None
    """Number of employees (headcount)."""

    operating_margin: Optional[float] = None
    """Operating margin (%). Operating income ÷ revenue."""

    payout_ratio: Optional[float] = None
    """Dividend payout ratio (%)."""

    pe_ratio: Optional[float] = None
    """Price-to-earnings ratio."""

    period_end: Optional[str] = None
    """Last day of the fiscal period (ISO 8601)."""

    roa: Optional[float] = None
    """Return on assets (%). Net income ÷ average total assets."""

    roe: Optional[float] = None
    """Return on equity (%). Net income ÷ average equity."""
