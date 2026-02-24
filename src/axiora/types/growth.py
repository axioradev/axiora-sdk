# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .growth_metrics import GrowthMetrics

__all__ = ["Growth", "Cagr", "Yoy"]


class Cagr(BaseModel):
    api_3yr: Optional[GrowthMetrics] = FieldInfo(alias="3yr", default=None)

    api_5yr: Optional[GrowthMetrics] = FieldInfo(alias="5yr", default=None)


class Yoy(BaseModel):
    fiscal_year: int

    growth: GrowthMetrics

    period_end: Optional[str] = None


class Growth(BaseModel):
    cagr: Cagr

    yoy: List[Yoy]
