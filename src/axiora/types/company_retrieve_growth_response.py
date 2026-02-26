# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .meta import Meta
from .growth import Growth
from .._models import BaseModel

__all__ = ["CompanyRetrieveGrowthResponse"]


class CompanyRetrieveGrowthResponse(BaseModel):
    data: Growth
    """The requested resource object."""

    meta: Meta
    """Request metadata."""
