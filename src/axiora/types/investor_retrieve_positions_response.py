# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["InvestorRetrievePositionsResponse", "Data", "DataInvestor", "DataPosition"]


class DataInvestor(BaseModel):
    active_positions: Optional[int] = None

    edinet_code: Optional[str] = None

    name_en: Optional[str] = None

    name_jp: Optional[str] = None

    total_positions: Optional[int] = None


class DataPosition(BaseModel):
    delta_180d_pct: Optional[float] = None

    delta_1y_pct: Optional[float] = None

    delta_90d_pct: Optional[float] = None

    filing_count: Optional[int] = None

    first_date: Optional[str] = None

    issuer_name: Optional[str] = None

    issuer_name_jp: Optional[str] = None

    issuer_security_code: Optional[str] = None

    last_date: Optional[str] = None

    latest_holding_pct: Optional[float] = None

    points: Optional[List[Dict[str, object]]] = None

    purpose_category: Optional[str] = None

    streak_length: Optional[int] = None

    trajectory_type: Optional[str] = None

    velocity_pp_per_month: Optional[float] = None


class Data(BaseModel):
    """The requested resource object."""

    investor: Optional[DataInvestor] = None

    positions: Optional[List[DataPosition]] = None


class InvestorRetrievePositionsResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
