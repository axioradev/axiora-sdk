# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["WaitlistJoinResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    tier: str

    created_at: Optional[str] = None


class WaitlistJoinResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
