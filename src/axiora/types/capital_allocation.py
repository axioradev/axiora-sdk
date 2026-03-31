# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CapitalAllocation"]


class CapitalAllocation(BaseModel):
    classification: str
    """Returner, Hoarder, Reinvestor, Mixed, or Insufficient Data"""

    edinet_code: str
    """EDINET code"""

    capex_revenue_ratio: Optional[float] = None
    """Capex / Revenue ratio"""

    fcf: Optional[float] = None
    """Free cash flow (JPY)"""

    fiscal_year: Optional[int] = None
    """Fiscal year analyzed"""

    name: Optional[str] = None
    """Company name"""

    return_ratio: Optional[float] = None
    """Total returns / FCF"""

    sector: Optional[str] = None
    """Sector"""

    securities_code: Optional[str] = None
    """Securities code"""

    total_returns: Optional[float] = None
    """Dividends + buybacks (JPY)"""
