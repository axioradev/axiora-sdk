# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GrowthMetrics"]


class GrowthMetrics(BaseModel):
    eps: Optional[float] = None

    gross_profit: Optional[float] = None

    net_income: Optional[float] = None

    operating_income: Optional[float] = None

    revenue: Optional[float] = None

    total_assets: Optional[float] = None
