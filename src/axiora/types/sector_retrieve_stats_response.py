# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectorRetrieveStatsResponse", "Data", "DataAggregates"]


class DataAggregates(BaseModel):
    avg_net_income: Optional[float] = None

    avg_operating_margin: Optional[float] = None

    avg_revenue: Optional[float] = None

    avg_roa: Optional[float] = None

    avg_roe: Optional[float] = None

    max_revenue: Optional[int] = None

    min_revenue: Optional[int] = None

    total_net_income: Optional[int] = None

    total_revenue: Optional[int] = None


class Data(BaseModel):
    aggregates: DataAggregates

    company_count: int

    sector: str


class SectorRetrieveStatsResponse(BaseModel):
    data: Data

    meta: Meta
