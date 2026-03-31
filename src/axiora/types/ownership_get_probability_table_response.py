# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .meta import Meta
from .._models import BaseModel

__all__ = ["OwnershipGetProbabilityTableResponse", "Data", "DataBucket"]


class DataBucket(BaseModel):
    confidence_level: str
    """low (<10), medium (10-29), high (>=30)"""

    purpose_type: str
    """Purpose bucket: investment, strategic, activist, other"""

    sample_size: int
    """Number of trajectories in this bucket"""

    stake_range: str
    """Stake range bucket: <5%, 5-10%, 10-20%, 20-33%, 33%+"""

    streak_range: str
    """Streak length bucket: 1, 2-3, 4+"""

    p_exit_6m: Optional[float] = None
    """P(exiting within 6 months)"""

    p_reach_10pct: Optional[float] = None
    """P(ever reaching 10%)"""

    p_reach_20pct: Optional[float] = None
    """P(ever reaching 20%)"""

    p_reach_33pct: Optional[float] = None
    """P(ever reaching 33% blocking minority)"""


class Data(BaseModel):
    """The requested resource object."""

    buckets: List[DataBucket]
    """Per-bucket conditional probabilities"""

    total_trajectories: int
    """Total trajectories used to compute table"""

    api_model_version: Optional[str] = FieldInfo(alias="model_version", default=None)
    """Model version identifier"""


class OwnershipGetProbabilityTableResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
