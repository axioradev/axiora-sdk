# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipListSignalsResponse", "Data"]


class Data(BaseModel):
    confidence: float
    """Confidence score 0-1"""

    detected_date: date
    """Date the signal was detected"""

    filer_code: str
    """Canonical EDINET code of the filer"""

    issuer_security_code: str
    """Securities code of the issuer"""

    signal_type: str
    """Signal type: accumulation_streak, large_step_up, exit_below_5pct, etc."""

    delta_pct: Optional[float] = None
    """Change in percentage points"""

    filer_name: Optional[str] = None
    """Name of the filer (JP)"""

    filer_name_en: Optional[str] = None
    """English name of the filer"""

    holding_ratio_pct: Optional[float] = None
    """Holding ratio at signal time"""

    issuer_name: Optional[str] = None
    """Name of the issuer (JP)"""

    issuer_name_en: Optional[str] = None
    """English name of the issuer"""

    metadata: Optional[Dict[str, object]] = None
    """Signal-specific context (streak, purpose, filers)"""

    tier: Optional[int] = None
    """Signal tier: 1=actionable, 2=informational, 3=trivial"""


class OwnershipListSignalsResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
