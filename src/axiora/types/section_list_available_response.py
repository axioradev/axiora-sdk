# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .._models import BaseModel

__all__ = ["SectionListAvailableResponse"]


class SectionListAvailableResponse(BaseModel):
    data: object
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
