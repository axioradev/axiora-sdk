# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ScreenRetrieveParams"]


class ScreenRetrieveParams(TypedDict, total=False):
    fiscal_year: Optional[int]

    limit: int

    net_income_max: Optional[int]

    net_income_min: Optional[int]

    offset: int

    operating_income_max: Optional[int]

    operating_income_min: Optional[int]

    revenue_max: Optional[int]

    revenue_min: Optional[int]

    roa_max: Optional[float]

    roa_min: Optional[float]

    roe_max: Optional[float]

    roe_min: Optional[float]

    sector: Optional[str]

    sort: str
