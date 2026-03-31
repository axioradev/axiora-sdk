# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectionListAvailableResponse"]


class SectionListAvailableResponse(BaseModel):
    data: Dict[str, object]
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
