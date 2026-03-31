# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipListCrossHoldingsResponse", "Data"]


class Data(BaseModel):
    a_holds_b_pct: float
    """A's holding ratio in B (%)"""

    b_holds_a_pct: float
    """B's holding ratio in A (%)"""

    company_a_edinet_code: str
    """EDINET code of company A"""

    company_b_edinet_code: str
    """EDINET code of company B"""

    relationship_type: str
    """mutual or asymmetric"""

    cluster_id: Optional[int] = None
    """Cluster grouping ID"""

    company_a_name: Optional[str] = None
    """Name of company A"""

    company_a_securities_code: Optional[str] = None
    """Securities code of company A"""

    company_b_name: Optional[str] = None
    """Name of company B"""

    company_b_securities_code: Optional[str] = None
    """Securities code of company B"""


class OwnershipListCrossHoldingsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
