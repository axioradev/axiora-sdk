# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .meta import Meta
from .._models import BaseModel

__all__ = ["WatchlistListResponse", "Data"]


class Data(BaseModel):
    id: int

    entity_code: str

    entity_type: str

    created_at: Optional[str] = None

    entity_name: Optional[str] = None


class WatchlistListResponse(BaseModel):
    data: List[Data]
    """Array of result objects."""

    meta: Meta
    """Pagination and request metadata."""
