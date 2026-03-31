# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...meta import Meta
from ...._models import BaseModel

__all__ = ["TrajectoryGetProbabilitiesResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    confidence_level: Optional[str] = None
    """low, medium, or high"""

    exit_within_6m: Optional[float] = None
    """P(exiting within 6 months)"""

    api_model_type: Optional[str] = FieldInfo(alias="model_type", default=None)
    """Model used: base_rate or coxph"""

    reach_10pct: Optional[float] = None
    """P(reaching 10%)"""

    reach_20pct: Optional[float] = None
    """P(reaching 20%)"""

    reach_33pct: Optional[float] = None
    """P(reaching 33% blocking minority)"""

    sample_size: Optional[int] = None
    """Number of historical trajectories in matching bucket"""


class TrajectoryGetProbabilitiesResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
