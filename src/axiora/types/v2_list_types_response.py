# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["V2ListTypesResponse", "Meta"]


class Meta(BaseModel):
    caveats: Optional[List[str]] = None

    data_as_of: Optional[str] = None
    """Source data date of the snapshot served."""

    data_version: Optional[str] = None
    """Snapshot version served."""

    deprecations: Optional[List[Dict[str, object]]] = None

    next_cursor: Optional[str] = None

    request_id: str

    resolved_from: Optional[str] = None
    """The identifier sent, when it was not the canonical id in data.id."""


class V2ListTypesResponse(BaseModel):
    data: Dict[str, object]

    meta: Meta
