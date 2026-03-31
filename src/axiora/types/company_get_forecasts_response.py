# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["CompanyGetForecastsResponse", "Data"]


class Data(BaseModel):
    accounting_standard: Optional[str] = None

    company_name: Optional[str] = None

    filing_date: Optional[str] = None

    fiscal_year_end: Optional[str] = None

    forecast_eps: Optional[float] = None

    forecast_net_income: Optional[int] = None

    forecast_net_income_change_pct: Optional[float] = None

    forecast_operating_income: Optional[int] = None

    forecast_operating_income_change_pct: Optional[float] = None

    forecast_ordinary_income: Optional[int] = None

    forecast_revenue: Optional[int] = None

    forecast_revenue_change_pct: Optional[float] = None

    period_type: Optional[str] = None

    securities_code: Optional[str] = None


class CompanyGetForecastsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
