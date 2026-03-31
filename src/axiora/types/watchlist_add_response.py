# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["WatchlistAddResponse", "Data"]


class Data(BaseModel):
    """The requested resource object."""

    id: int

    entity_code: str

    entity_type: str

    created_at: Optional[str] = None

    entity_name: Optional[str] = None


class WatchlistAddResponse(BaseModel):
    data: Data
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
