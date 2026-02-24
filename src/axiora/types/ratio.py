# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Ratio"]


class Ratio(BaseModel):
    fiscal_year: int

    bps: Optional[float] = None

    debt_to_equity: Optional[float] = None

    dividends_per_share: Optional[float] = None

    eps: Optional[float] = None

    equity_ratio: Optional[float] = None

    net_margin: Optional[float] = None

    num_employees: Optional[int] = None

    operating_margin: Optional[float] = None

    payout_ratio: Optional[float] = None

    pe_ratio: Optional[float] = None

    period_end: Optional[str] = None

    roa: Optional[float] = None

    roe: Optional[float] = None
