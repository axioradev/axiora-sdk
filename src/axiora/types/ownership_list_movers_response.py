# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipListMoversResponse", "Data"]


class Data(BaseModel):
    filer_canonical_code: str
    """Canonical EDINET code of the filer"""

    issuer_security_code: str
    """Securities code of the issuer"""

    trajectory_type: str
    """accumulating or exiting"""

    velocity_pp_per_month: float
    """Percentage points change per month"""

    delta_90d_pct: Optional[float] = None
    """Change over 90 days"""

    filer_name: Optional[str] = None
    """Name of the filer (JP)"""

    filer_name_en: Optional[str] = None
    """English name of the filer"""

    issuer_name: Optional[str] = None
    """Name of the issuer (JP)"""

    issuer_name_en: Optional[str] = None
    """English name of the issuer"""

    last_base_date: Optional[date] = None
    """Date of most recent filing"""

    latest_holding_ratio_pct: Optional[float] = None
    """Latest holding ratio"""

    purpose_category: Optional[str] = None
    """Latest classified purpose"""


class OwnershipListMoversResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
