# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipListUnwindingScoreboardResponse", "Data"]


class Data(BaseModel):
    company_a_edinet_code: str
    """EDINET code of company A"""

    company_b_edinet_code: str
    """EDINET code of company B"""

    unwinding_status: str
    """mutual_unwinding, one_sided_exit, gradual_decline, monitoring"""

    a_delta_90d_pct: Optional[float] = None
    """A's 90-day change"""

    a_holds_b_pct: Optional[float] = None
    """A's holding in B (%)"""

    a_trajectory_type: Optional[str] = None
    """A's trajectory type"""

    a_velocity_pp_per_month: Optional[float] = None
    """A's pace (pp/month)"""

    b_delta_90d_pct: Optional[float] = None
    """B's 90-day change"""

    b_holds_a_pct: Optional[float] = None
    """B's holding in A (%)"""

    b_trajectory_type: Optional[str] = None
    """B's trajectory type"""

    b_velocity_pp_per_month: Optional[float] = None
    """B's pace (pp/month)"""

    company_a_name: Optional[str] = None
    """Name of company A"""

    company_a_securities_code: Optional[str] = None
    """Securities code of company A"""

    company_b_name: Optional[str] = None
    """Name of company B"""

    company_b_securities_code: Optional[str] = None
    """Securities code of company B"""


class OwnershipListUnwindingScoreboardResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
